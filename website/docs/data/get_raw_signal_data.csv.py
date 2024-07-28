from h5py import File
import numpy as np
import pandas as pd
import sys
# OpenSignals Tools own package for loading and plotting the acquired data
import biosignalsnotebooks as bsnb
import biosignalsnotebooks.signal_samples as bsnb_ss
import scipy as sp
import os
from scipy import signal

folder = '/Users/htr365/Documents/Side_Projects/09_founding_lab/amanda_johanna/archiv/Muscle Data/muscle_data/Vastus Lateralis Left'

files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".h5")]

def read_raw_signal(file):
    # get raw signal
    data, header = bsnb_ss.load(file, get_header=True)
    ch = "CH1" # Channel
    sr = header["sampling rate"] # Sampling rate
    resolution = header["resolution"] 
    signal = data[ch]

    # Baseline shift.
    signal = np.array(signal) - np.mean(signal)

    # create bandpass filter for EMG
    high = 20/(1000/2)
    low = 5000/(1000/2)
    b, a = sp.signal.butter(4, [high,low], btype='bandpass')

    # process EMG signal: filter EMG
    signal = sp.signal.filtfilt(b, a, signal)
    
    # rectify
    signal = abs(signal)

    time = bsnb.generate_time(signal,sr)
    numbers = re.findall(r'\d+', file)
    name = [int(num) for num in numbers]
    year_idx = [i for i, num in enumerate(name) if np.isin(num,[2023,2024])][0]
    year,month,day,hour,minu = name[year_idx:year_idx+5]
    #raw_signal_data = pd.DataFrame([time,signal,np.repeat(name,len(signal))]).T.rename(columns={0:'time',1:'signal'})
    return pd.DataFrame([np.array(time),signal,np.repeat(year,len(signal)), 
    np.repeat(month,len(signal)),np.repeat(day,len(signal)),
    np.repeat(hour,len(signal))]).T.rename(columns={0:'time',1:'signal',2:'year',3:'month',4:'day',5:'hour'})
    #[np.array(time),signal]
    #return raw_signal_data


all_data = pd.DataFrame()
for file in files:
    all_data = pd.concat([all_data,read_raw_signal(file)])
all_data.to_csv(sys.stdout)
#pd.DataFrame(signal).to_csv(sys.stdout)