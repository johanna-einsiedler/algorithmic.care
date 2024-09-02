
import sys
import os
import pandas as pd
import numpy as np
import biosignalsnotebooks as bsnb
import biosignalsnotebooks.signal_samples as bsnb_ss
import re
import pickle
import scipy as sp
from datetime import datetime, timedelta


def read_raw_signal(file):
    # get raw signal
    data, header = bsnb_ss.load(file, get_header=True)
    sr = header["sampling rate"] # Sampling rate
    resolution = header["resolution"] 
    signal_emg = data['CH1']
    signal_mmg = data['CH2']

    # Baseline shift.
    signal_emg = np.array(signal_emg) - np.mean( signal_emg)
    signal_mmg = np.array(signal_mmg) - np.mean( signal_mmg)

    # create bandpass filter for EMG of order 4
    signal_emg = bsnb.bandpass(signal_emg,f1=20,f2=450,  order=4, fs=1000,use_filtfilt=True)
    signal_mmg = bsnb.bandpass(signal_mmg,f1=2,f2=50,  order=4, fs=1000,use_filtfilt=True)

    # rectify
    signal_emg = abs(signal_emg)
    signal_mmg = abs(signal_mmg)

    # amplitude normalization
    signal_emg = signal_emg/np.max(signal_emg)
    signal_mmg = signal_mmg/np.max(signal_mmg)
    
    # get time indicators
    time = bsnb.generate_time(signal_emg,sr)
    numbers = re.findall(r'\d+', file)
    name = [int(num) for num in numbers]
    year_idx = [i for i, num in enumerate(name) if np.isin(num,[2023,2024])][0]
    year,month,day,hour,minu = name[year_idx:year_idx+5]
    #raw_signal_data = pd.DataFrame([time,signal,np.repeat(name,len(signal))]).T.rename(columns={0:'time',1:'signal'})
    df = pd.DataFrame([np.array(time),signal_emg,signal_mmg, np.repeat(year,len(signal_emg)), 
    np.repeat(month,len(signal_emg)),np.repeat(day,len(signal_emg)),
    np.repeat(hour,len(signal_emg))]).T.rename(columns={0:'time',1:'signal_emg',2:'signal_mmg',3:'year',4:'month',5:'day',6:'hour'})

    # create date variable
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day','hour']])

      # create AM / PM indicator
    df['am_pm'] = 'AM'
    df.loc[df['hour']>12,'am_pm'] = 'PM'

    # if hour is before 4am use it as measurement from day before
    df.loc[df['hour']<4,'date'] = df.loc[df['hour']<4,'date'] -timedelta(days=1)
    df.loc[df['hour']<4,'am_pm'] = 'PM'

    # apply burst detection algorithm
    burst_begin, burst_end = bsnb.detect_emg_activations(df['signal_emg'],sr, smooth_level=20, threshold_level=10, 
                                                        time_units=True)[:2]
                                               
    startTabata = burst_begin[burst_begin>30][0]  -30

    df = df[df['time']>startTabata]
    df.loc[df['time']<startTabata+ 30,'interval'] = 'sit_relaxed_1'
    df.loc[(startTabata+30<df['time'])*(df['time']<startTabata+36),'interval'] = 'muscle_contraction_1'
    df.loc[(startTabata+36<df['time'])*(df['time']<startTabata+46),'interval'] = 'rest_1'
    df.loc[(startTabata+46<df['time'])*(df['time']<startTabata+52),'interval'] = 'muscle_contraction_2'
    df.loc[(startTabata+52<df['time'])*(df['time']<startTabata+62),'interval'] = 'rest_2'
    df.loc[(startTabata+62<df['time'])*(df['time']<startTabata+68),'interval'] = 'muscle_contraction_3'
    df.loc[(startTabata+68<df['time'])*(df['time']<startTabata+88),'interval'] = 'prep_wallsit'
    df.loc[(startTabata+88<df['time'])*(df['time']<startTabata+108),'interval'] = 'wallsit'
    df.loc[(startTabata+108<df['time'])*(df['time']<startTabata+123),'interval'] = 'sit_down'
    df.loc[(startTabata+123<df['time'])*(df['time']<startTabata+153),'interval'] = 'sit_relaxed_2'
    df = df[df['time']<153]

    # add markers for protocol 
    # -> add 'burn in' time & 'fade out' time of 1 s for contractions
   # df.loc[df['time']<30,'interval'] = 'sit_relaxed_1'
    # 1s burn in time + 1s fade out time -> i.e. only take the middle 4s of 6s contraction
    #df.loc[(31<df['time'])*(df['time']<35),'interval'] = 'muscle_contraction_1'
    # 1s burn in time + 1s fade out time -> i.e. only take the middle 8s of 10s rest
    #df.loc[(37<df['time'])*(df['time']<45),'interval'] = 'rest_1'
    # 1s burn in time + 1s fade out time -> i.e. only take the middle 4s of 6s contraction
    #df.loc[(47<df['time'])*(df['time']<51),'interval'] = 'muscle_contraction_2'
    # 1s burn in time + 1s fade out time -> i.e. only take the middle 8s of 10s rest
    #df.loc[(53<df['time'])*(df['time']<61),'interval'] = 'rest_2'
    # 1s burn in time + 1s fade out time -> i.e. only take the middle 4s of 6s contraction
    #df.loc[(63<df['time'])*(df['time']<67),'interval'] = 'muscle_contraction_3'
    #df.loc[(68<df['time'])*(df['time']<88),'interval'] = 'prep_wallsit'
    #df.loc[(88<df['time'])*(df['time']<108),'interval'] = 'wallsit'
    #df.loc[(108<df['time'])*(df['time']<123),'interval'] = 'sit_down'
    #df.loc[(123<df['time'])*(df['time']<153),'interval'] = 'sit_relaxed_2'
    #df.loc[df['time']>133,'interval'] = 'end'

    
    #df.loc[df['interval']== interval,'rms'] = rms_envelope

    # add markers for switch of interval
    #df['marker'] = 0
    #df.loc[[36,46,52,62,68,88,108,123],'marker'] = 1

    return df





if __name__ == "__main__":
    # get file path
    path = sys.argv[1]
    print(path)
    print('JE' in path)
    new_path =  '../../../data/data_pre_processed/JE/' if 'JE' in path else '../../../data/data_pre_processed/AB/'

    if os.path.isfile(path):
        df = read_raw_signal(path)
        with open(new_path+(df['date'].astype(str)+'_'+df['am_pm']).unique()[0]+'.pickle', 'wb') as handle:
            pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if os.path.isdir(path):
        items = os.listdir(path)
        # Filter out only files
        files = [f for f in items if os.path.isfile(os.path.join(path, f))]
        for file in files:
            if file.endswith(".h5"):
                df = read_raw_signal(os.path.join(path,file))
                with open(new_path+(df['date'].astype(str)+'_'+df['am_pm']).unique()[0]+'.pickle', 'wb') as handle:
                    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print('success')