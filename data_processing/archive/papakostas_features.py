# import all the libraries we need
import os
from skimage import util
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pywt
import matplotlib.pyplot as plt
from utils import mtFeatureExtraction


# Michalis Papakostas, Varun Kanal, Maher Abujelala, Konstantinos Tsiakas, and Fillia Makedon. 2019. Physical fatigue detection through EMG wearables and subjective user reports: 
# a machine learning approach towards adaptive rehabilitation.
# In Proceedings of the 12th ACM International Conference on PErvasive Technologies Related to Assistive Environments (PETRA '19). Association for Computing Machinery,
# New York, NY, USA, 475–481. https://doi.org/10.1145/3316782.3322772



# extract midterm features for all observations
def getMidTermFeatures(df):

    # get sampling frequency, i.e. number of samples obtained in one second
    samplingFrequency = df['sr'][0]

    # short-term window size
    stWindowSize = 0.25*samplingFrequency
    #short-term overlap
    stStep = stWindowSize

    # mid-term window size
    mtWindowSize = 2*samplingFrequency
    mtStep = mtWindowSize - 1*samplingFrequency
    all_features = pd.DataFrame()

    for i in range(df.shape[0]):
        id = i
        mtFeatures = mtFeatureExtraction(df['signal'][i],samplingFrequency, mtWindowSize, mtStep, stWindowSize, stStep)
        output_i = pd.DataFrame(mtFeatures[0].T)
        output_i['id'] = i
        all_features = pd.concat([all_features, output_i])
    return(all_features)


if __name__ == "__main__":
    current_path = os.path.dirname( __file__ )
    df = pd.read_pickle(os.path.join(current_path, '../data/muscle_data.pkl'))
    features = getMidTermFeatures(df)
    features.to_pickle(os.path.join(current_path,'../data/features_papakostas.pkl'))
