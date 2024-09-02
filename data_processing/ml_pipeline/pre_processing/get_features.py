import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pywt
import scipy as sp
import pickle
import os
import sys
import biosignalsnotebooks as bsnb

intervals = ['sit_relaxed_1','muscle_contraction_1','rest_1','muscle_contraction_2','rest_2','muscle_contraction_3','prep_wallsit','wallsit','sit_down','sit_relaxed_2']
print(os.getcwd())
sys.path.append('../utils')


# importing
from feature_extraction_functions import *


def get_emg_features(input, frame, step):

    #frame =250
    #step = 25
    # calculate envelope 
    # https://scientificallysound.org/2016/08/22/python-analysing-emg-signals-part-4/
    sr = 1000
    #low_pass = 1
    #low_pass = low_pass/(sr/2)
    #b2, a2 = sp.signal.butter(4, low_pass, btype='lowpass')
    if isinstance(input, str):
    # read in data
        df = pd.read_pickle(input)
    else:
        df =input

    # cut off end to make it equally long
    #df = df[df['time'] <=153]
    #df['emg_envelope'] = sp.signal.filtfilt(b2, a2, df['signal_emg'])


    df_features_emg = features_estimation(df['signal_emg'], 'EMG', sr, frame,step, plot=False)[0]
    df_features_emg = df_features_emg.transpose()
    df_features_emg.loc[:,'interval'] = np.nan

    df_features_mmg = features_estimation(df['signal_mmg'], 'MMG', sr, frame, step, plot=False)[0]
    df_features_mmg = df_features_mmg.transpose()
    df_features = pd.concat([df_features_emg,df_features_mmg.drop(['START','END'],axis=1)],axis=1)

    # apply burst detection algorithm
    burst_begin, burst_end = bsnb.detect_emg_activations(df['signal_emg'],sr, smooth_level=20, threshold_level=10, 
                                                        time_units=True)[:2]
    # get start of first burst as reference
    startTabata = burst_begin[burst_begin>30][0]  -30

    df_features = df_features[df_features['END']>startTabata]
    df_features.loc[df_features['END']/1000<startTabata+ 30,'interval'] = 'sit_relaxed_1'
    df_features.loc[(startTabata+30<df_features['START']/1000)*(df_features['END']/1000<startTabata+36),'interval'] = 'muscle_contraction_1'
    df_features.loc[(startTabata+36<df_features['START']/1000)*(df_features['END']/1000<startTabata+46),'interval'] = 'rest_1'
    df_features.loc[(startTabata+46<df_features['START']/1000)*(df_features['END']/1000<startTabata+52),'interval'] = 'muscle_contraction_2'
    df_features.loc[(startTabata+52<df_features['START']/1000)*(df_features['END']/1000<startTabata+62),'interval'] = 'rest_2'
    df_features.loc[(startTabata+62<df_features['START']/1000)*(df_features['END']/1000<startTabata+68),'interval'] = 'muscle_contraction_3'
    df_features.loc[(startTabata+68<df_features['START']/1000)*(df_features['END']/1000<startTabata+88),'interval'] = 'prep_wallsit'
    df_features.loc[(startTabata+88<df_features['START']/1000)*(df_features['END']/1000<startTabata+108),'interval'] = 'wallsit'
    df_features.loc[(startTabata+108<df_features['START']/1000)*(df_features['END']/1000<startTabata+123),'interval'] = 'sit_down'
    df_features.loc[(startTabata+123<df_features['START']/1000)*(df_features['END']/1000<startTabata+153),'interval'] = 'sit_relaxed_2'
    df_features = df_features[df_features['END']/1000<153]
    return df_features



if __name__ == "__main__":
    # get file path
    path = sys.argv[1]
    frame = sys.argv[2]
    step = sys.argv[3]
    new_path =  '../../../data/data_features/JE/' if 'JE' in path else '../../../data/data_features/AB/'

    if os.path.isfile(path):
        df = get_emg_features(path, int(frame), int(step))
        with open(new_path+path.split('/')[-1].split('.')[0]+'.pickle', 'wb') as handle:
            pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if os.path.isdir(path):
        items = os.listdir(path)
        # Filter out only files
        files = [f for f in items if os.path.isfile(os.path.join(path, f))]
        df = get_emg_features(os.path.join(path,files[0]), int(frame), int(step))

        for file in files:
            try:
               df = get_emg_features(os.path.join(path,file), int(frame), int(step))
               with open(new_path+file.split('/')[-1].split('.')[0]+'.pickle', 'wb') as handle:
                    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
            except:
               print("error couldn't save " + file )
               next

    print('success')