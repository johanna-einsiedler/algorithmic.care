# import all the libraries we need
import os
from skimage import util
import pandas as pd
from scipy.integrate import cumtrapz
import numpy as np
from scipy.signal import welch
import biosignalsnotebooks as bsnb
from utils import extract_signal, extract_fatigue

#path = os.path.abspath(os.path.join(current_path, '../data/'))


#Extract "fatigue" measure i.e. median power frequency as described in the "Fatigue Evaluation - Evolution of Median Power Frequency" Notebook from biosignals: 
# http://notebooks.pluxbiosignals.com/notebooks/Categories/Pre-Process/emg_fatigue_evaluation_median_freq_rev.html


def getFatigue(df):
 
    #sprint(df)
    # get sampling frequency, i.e. number of samples obtained in one second
    samplingFrequency = df['sr'][0]

    median_freq_data = pd.DataFrame(list(map(extract_fatigue,df['signal'],np.repeat(samplingFrequency,df.shape[0]))))
    median_freq_data = median_freq_data.rename(columns={0:'mean_median_freq',1:'max_median_freq',2:"median_freq_list"})
    return(median_freq_data)


#Get features like described in http://notebooks.pluxbiosignals.com/notebooks/Categories/Extract/emg_parameters_rev.html

def getBitalinoFeatures(df):
    # calculate number of bursts
    fs = df['sr'][0]
    bursts = []
    for i in range(df.shape[0]):
        signal = df['signal'][i]
        burst_begin, burst_end = bsnb.detect_emg_activations(signal,fs, smooth_level=20, threshold_level=10, 
                                                        time_units=True)[:2]
        # Bursts Duration
        bursts_time = burst_end - burst_begin

        # Parameter extraction
        max_time = max(bursts_time)
        min_time = min(bursts_time)
        avg_time = np.average(bursts_time)
        std_time = np.std(bursts_time)

        # Sample Stats
        # Maximum
        max_sample_value = max(signal)
        # Minimum
        min_sample_value = min(signal)

        # Average and Standard Deviation
        avg_sample_value = np.average(signal)
        std_sample_value = np.std(signal)

        # Root Mean Square
        rms = np.sqrt(sum(signal * signal) / len(signal))

        # Area under the curve
        area = cumtrapz(signal)[-1]

        # Signal Power Spectrum
        f, P = welch(signal, fs=fs, window='hamming', noverlap=0, nfft=int(256.))

        # Total Power and Median Frequency (Frequency that divides the spectrum into two regions with equal power)
        area_freq = cumtrapz(P, f, initial=0)
        total_power = area_freq[-1]
        median_freq = f[where(area_freq >= total_power / 2)[0][0]]
        f_max = f[np.argmax(P)]
        bursts.append([len(burst_begin),avg_time, max_time,min_time,std_time,
                    avg_sample_value,max_sample_value, min_sample_value, std_sample_value,
                    area, total_power, median_freq,f_max])
        bursts = pd.DataFrame(bursts).rename(columns ={0:'bursts_count',1:'avg_time',2:'max_time',3:'min_time',4:'std_time',
                                      5:'avg_sample_value',6:'max_sample_value',7:'min_sample_value',8:'std_sample_value',
                                      9:'area',10:'total_power',11:'median_freq',12:'f_max'})
        return(bursts)

if __name__ == "__main__":
    #path = sys.argv[1]
    #getBitalinoFeatures()
    current_path = os.path.dirname( __file__ )
    df = pd.read_pickle(os.path.join(current_path, '../data/muscle_data.pkl'))
    df_fatigue = getFatigue(df)
    df_bitalino = getBitalinoFeatures(df)

    df_all = df_fatigue.merge(df_bitalino, left_index=True, right_index=True)
    df_all.to_pickle(os.path.join(current_path,'../data/features_bitalino.pkl'))
    