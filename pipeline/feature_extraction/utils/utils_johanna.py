# import all the libraries we need
import os
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

# OpenSignals Tools own package for loading and plotting the acquired data
import biosignalsnotebooks as bsnb
import biosignalsnotebooks.signal_samples as bsnb_ss


# function to extract all numbers from a string -> used to get the date out of the file name
def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    return [int(num) for num in numbers]


# for each measurement calculate the median frequency 
# from biosignals notebooks docs:
#  The median frequency of activation events in EMG signal is particularly important in fatigue evaluation methods.
#This function calculates the median frequency of each activation period and allows to plot those values in order to
#see the temporal evolution of this particular feature.

def extract_signal(file):
    # get date
    numbers_in_name = extract_numbers(file)

    # find index of year
    #year_idx = [i for i, num in enumerate(numbers_in_name) if np.isin(num,[2023,2024])][0]
    #year,month,day,hour,minu = numbers_in_name[year_idx:year_idx+5]

    data, header = bsnb_ss.load(file, get_header=True)
    channel1 = "CH" + str(header["channels"][0])
    #channel2 = "CH" + str(header["channels"][1])

    # Sampling rate and acquired data
    sr = header["sampling rate"]

    # Signal Samples
    signal1 = data[channel1]
    #signal2 = data[channel2]

    time = linspace(0, len(signal1) / sr, len(signal1))

    return [ signal1, sr, time,file]

def extract_fatigue(signal,sr):
    # calculate fatigue level per activation period
    #fatigue = bsnb.fatigue_eval_med_freq(signal, sr)
    activation_begin, activation_end = bsnb.detect_emg_activations(signal, sr)[:2]
    # Iteration along muscular activations
    median_freq_data = []
    median_freq_time = []
    for activation in range(0, len(activation_begin)):
        processing_window = signal[activation_begin[activation]:activation_end[activation]]
        central_point = (activation_begin[activation] + activation_end[activation]) / 2
        median_freq_time += [central_point / sr]

        # Processing window power spectrum (PSD) generation
        freqs, power = periodogram(processing_window, fs=sr)

        # Median power frequency determination
        area_freq = cumtrapz(power, freqs, initial=0)
        total_power = area_freq[-1]
        median_freq_data += [freqs[where(area_freq >= total_power / 2)[0][0]]]

    # calculate mean and max frequency per measurement occasion
    #mean_fatigue = np.mean(fatigue['Median Frequency (Hz)'])
    #max_fatigue = np.max(fatigue['Median Frequency (Hz)'])
    mean_fatigue = np.mean(median_freq_data)
    max_fatigue = np.max(median_freq_data)
    measurement_data = [mean_fatigue,max_fatigue,list(median_freq_data)]
    return measurement_data