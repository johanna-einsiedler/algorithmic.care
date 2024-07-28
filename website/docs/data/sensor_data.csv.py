import os
import numpy as np
import sys
import pandas as pd
import re

# OpenSignals Tools own package for loading and plotting the acquired data
import biosignalsnotebooks as bsnb
import biosignalsnotebooks.signal_samples as bsnb_ss

folder = os.path.abspath('/sensor_data/')
files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".h5")]
print(files)



def read_raw_signal(file,channel=1):
    # get raw signal
    data, header = bsnb_ss.load(file, get_header=True)
    if channel==1:
        ch = "CH1" # Channel
    if channel ==2:
        ch = 'CH2'
    sr = header["sampling rate"] # Sampling rate
    resolution = header["resolution"] 
    signal = data[ch]

     # Baseline shift.
    signal = np.array(signal) - np.mean(signal)

    # create bandpass filter for EMG of order 4
    signal = bsnb.bandpass(signal,f1=20,f2=450,  order=4, fs=1000,use_filtfilt=True)
    
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
    #return raw_signal_data\


emg_signal1 = read_raw_signal(files[0])
pd.DataFrame(emg_signal1).to_csv(sys.stdtout)


