import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
# cnn model
from numpy import mean
from numpy import std
from numpy import dstack
from pandas import read_csv
from matplotlib import pyplot as plt
import glob

# filter only muscle contractions and only take the 2s in the middle
def filter_muscle_contractions(df):
   start = df.loc[df['interval']=='muscle_contraction_1','START'].iloc[0]/1000 -30

   #print(start_m1)
   contraction_1 = df[(df['START']/1000 >start+31) * (df['END']/1000 <start+34)]
   contraction_2 = df[(df['START']/1000 >start+47) * (df['END']/1000 <start+50)]
   contraction_3 = df[(df['START']/1000 >start+63) * (df['END']/1000 <start+66)]

   return pd.concat([contraction_1,contraction_2,contraction_3])

# filter only tak relax and only take from 15s in until 5s before end
def filter_relax(df):
   start = df.loc[df['interval']=='muscle_contraction_1','START'].iloc[0]/1000 -30
   relax_1 = df[(df['START']/1000 >start+15) * (df['END']/1000 <start+25)]
   relax_2 = df[(df['START']/1000 >start+138) * (df['END']/1000 <start+148)]

   return pd.concat([relax_1, relax_2]).drop('interval',axis=1)

# take intermediate 10s of wallsit
def filter_wallsit(df):
   start = df.loc[df['interval']=='muscle_contraction_1','START'].iloc[0]/1000 -30
   #print(start)
   wallsit = df[(df['START']/1000 >start+93) * (df['END']/1000 <start+103)]

   return wallsit.drop('interval',axis=1)

def get_dates(person, survey, emg_path, outcome = None):
    # get survey only for one person
    sub_survey = survey[survey['person']==person]
    # subset to days where outcome is not nan
    if outcome is not None:
        sub_survey = sub_survey[~np.isnan(sub_survey[outcome])]
    # get all available dates
    dates = sub_survey['date']
    # get all dates where we have emg data for that person
    if person == 'Johanna':
        suffix = 'JE'
    else:
        suffix = 'AB'
    files = glob.glob(os.path.join(emg_path+suffix+'/', '*.pickle'))
    dates_emg = [x.split('/')[-1].split('_')[0] for x in files]
    timing_emg = [x.split('/')[-1].split('_')[1].split('.')[0] for x in files]
    df_dates = pd.concat([pd.Series(dates_emg),pd.Series(timing_emg)],axis=1)
    df_dates['person'] = person
    return df_dates[np.isin(dates_emg,dates)].rename(columns={0:'date',1:'timing'})

def data_loader(indicators,survey,emg_path, interval =None, outcome = None):

    # dict for combining different intervals of same activity
    position_dict = {'sit_relaxed_1': 'relaxed',
    'muscle_contraction_1':'muscle_contraction',
    'muscle_contraction_2':'muscle_contraction',
    'muscle_contraction_3':'muscle_contraction',
    'wallsit':'wallsit',
    'sit_relaxed_2': 'relaxed'}



    data = pd.DataFrame()
    for index, row in indicators.iterrows():
        if row['person'] == 'Amanda':
            folder_indicator = 'AB'
        else:
            folder_indicator = 'JE'

        # Get a list of all files in the directory
        files = os.listdir(emg_path + folder_indicator+'/')
        # Filter the files for the specific date
        matching_files = glob.glob(os.path.join(emg_path + folder_indicator+'/', f"{row['date']}*"))
        for file in matching_files:
            df = pd.read_pickle(file)
            df['person'] = row['person']
            df['date'] = row['date']
            df['timing'] = file.split('/')[-1].split('_')[1].split('.')[0]
            df['interval_combined'] = df['interval'].map(position_dict)

            # get dummies for interval
            df = pd.concat([df, pd.get_dummies(df['interval'], dtype=int)[:-1]],axis=1)

            # get dummies for person
            # if specified filter only certain interval type
            if interval =='relax':
                df = filter_relax(df)
            if interval =='contraction':
                df = filter_muscle_contractions(df)
            if interval =='wallsit':
                df = filter_wallsit(df)
            if outcome is not None:
                y = survey[(survey['person'] ==row['person'])*(survey['date']==row['date'])][outcome]
                df[outcome] = y.iloc[0]
            data = pd.concat([data,df],axis=0)
    data = pd.concat([data, pd.get_dummies(data['person'], dtype=int).iloc[:,0]],axis=1)
    data = pd.concat([data, pd.get_dummies(data['timing'], dtype = int, ).iloc[:,0]],axis=1)

    return data