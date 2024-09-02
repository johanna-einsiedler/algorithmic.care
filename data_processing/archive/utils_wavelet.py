import numpy as np
import pywt
from sklearn.preprocessing import StandardScaler

import scipy
from scipy.stats import kurtosis
from scipy.stats import skew #skewness
from collections import defaultdict, Counter
from scipy.stats import kurtosis
from scipy.stats import skew


def wave_length(x):
    x = np.array(x)
    x = np.append(x[-1], x)
    x = np.append(x,x[1])
    xn = x[1:len(x)-1]
    xn_i2 = x[2:len(x)]    # xn+1 
    return sum(abs(xn_i2-xn))
    
def norm_entropy(x):
    tresh = 2
    return sum(np.power(abs(x),tresh))

def SRAV(x):    
    SRA = sum(np.sqrt(abs(x)))
    return np.power(SRA/len(x),2)

def mean_abs(x):
    return sum(abs(x))/len(x)


def _kurtosis(x):
    return kurtosis(x)

def CPT5(x):
    den = len(x)*np.exp(np.std(x))
    return sum(np.exp(x))/den

def SSC(x):
    x = np.array(x)
    x = np.append(x[-1], x)
    x = np.append(x,x[1])
    xn = x[1:len(x)-1]
    xn_i2 = x[2:len(x)]    # xn+1 
    xn_i1 = x[0:len(x)-2]  # xn-1
    ans = np.heaviside((xn-xn_i1)*(xn-xn_i2),0)
    return sum(ans[1:]) 





def calculate_entropy(list_values):
    counter_values = Counter(list_values).most_common()
    probabilities = [elem[1]/len(list_values) for elem in counter_values]
    entropy=scipy.stats.entropy(probabilities)
    return entropy
 
def calculate_statistics(list_values):
    n5 = np.nanpercentile(list_values, 5)
    n25 = np.nanpercentile(list_values, 25)
    n75 = np.nanpercentile(list_values, 75)
    n95 = np.nanpercentile(list_values, 95)
    median = np.nanpercentile(list_values, 50)
    mean = np.nanmean(list_values)
    std = np.nanstd(list_values)
    var = np.nanvar(list_values)
    rms = np.nanmean(np.sqrt(list_values**2))
    # New features
    kur = kurtosis(list_values)
    MeanAbs = mean_abs(list_values)
    norm_ent = norm_entropy(list_values)
    skewness = skew(list_values)
    CPT_5 = CPT5(list_values)
    SSC_1 = SSC(list_values)
    WL = wave_length(list_values)
    SRAV_1 = SRAV(list_values)
    return [n5, n25, n75, n95, median, mean, std, var, rms, kur, MeanAbs, norm_ent, skewness, CPT_5, SSC_1, WL, SRAV_1]
 
def calculate_crossings(list_values):
    zero_crossing_indices = np.nonzero(np.diff(np.array(list_values) > 0))[0]
    no_zero_crossings = len(zero_crossing_indices)
    mean_crossing_indices = np.nonzero(np.diff(np.array(list_values) > np.nanmean(list_values)))[0]
    no_mean_crossings = len(mean_crossing_indices)
    return [no_zero_crossings, no_mean_crossings]


def get_features(list_values):
    entropy = calculate_entropy(list_values)
    crossings = calculate_crossings(list_values)
    statistics = calculate_statistics(list_values)
    return [entropy] + crossings + statistics    


def feature_extraction_wpd(data, level, samplingFrequency):
    # Sampling rate
    fs = samplingFrequency  
    seconds = 0.25
    corpus = []
    # Signal standarization
    data_std = StandardScaler().fit_transform(data.reshape(-1,1)).reshape(1,-1)[0]            
    
    # WPD tree
    wptree = pywt.WaveletPacket(data=data_std, wavelet='db5', mode='symmetric', maxlevel=level)
    levels = wptree.get_level(level, order = "freq")            
    
    #Feature extraction for each node
    features = []        
    for node in levels:
        data_wp = node.data
        # Features group
        features.extend(get_features(data_wp))
    corpus.append(features)
    # Delate first row
    return np.array(corpus)