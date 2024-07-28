# import all the libraries we need
import os
from skimage import util

import matplotlib.pyplot as plt
import pandas as pd
from numpy import linspace, where
from scipy.signal import periodogram
from scipy.integrate import cumtrapz
import numpy as np
import re
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import struct
import tsfresh
import neurokit2 as nk
import pywt
from tsfresh import extract_features
from scipy import signal, ndimage
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LogNorm, NoNorm
from matplotlib.cm import get_cmap
import sys
from scipy.integrate import cumtrapz
from scipy.signal import welch,butter, filtfilt

from utils import feature_extraction_wpd


#Kefalas, M. (2023, January 19). Data-driven predictive maintenance and time- series applications. 
#Retrieved from https://hdl.handle.net/1887/3511983

def calculate_mean(data, start_index,window_size):
    window_data = data[start_index:start_index+window_size]
    return window_data.mean()

def getFeatures(df):

    window_size=250
    # get sampling frequency, i.e. number of samples obtained in one second
    samplingFrequency = df['sr'][0]

    # extract midterm features for all observations
    all_features = pd.DataFrame()
    for i in range(df.shape[0]):
        id = i
        df_sub = pd.DataFrame(df['signal'][i]).reset_index().rename(columns={0:'value'})
        # aggreagte per 0.25 s
        aggregated_means=[]
        for j in range(0, df_sub.shape[0], window_size):
            aggregated_means.append(calculate_mean(df_sub['value'],j,window_size))
        aggregated_means = pd.DataFrame(aggregated_means).reset_index().rename(columns={0:'value'})
        output_i = extract_features(aggregated_means, column_id='index')
        output_i = pd.DataFrame(output_i)
        output_i['id'] = i
        all_features = pd.concat([all_features, output_i])
    return(all_features)

if __name__ == "__main__":#
    current_path = os.path.dirname( __file__ )
    df = pd.read_pickle(os.path.join(current_path, '../data/muscle_data.pkl'))
    features = getFeatures(df)
    features.to_pickle(os.path.join(current_path,'../data/features_kefalas.pkl'))