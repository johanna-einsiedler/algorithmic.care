from scipy.fftpack import fft
import sys

import scipy.misc
import os
import numpy as np
import glob
import scipy
#from pyAudioAnalysis import audioFeatureExtraction as aF
import matplotlib.patches
from PIL import Image
#import cv2
import matplotlib.cm
import scipy.signal as filter
#import pyAudioAnalysis.audioFeatureExtraction as audioFeatureExtraction
eps = 0.00000001



def mtFeatureExtraction(signal,Fs, mtWin, mtStep, stWin, stStep):
    """
    Mid-term feature extraction
    """

    mtWinRatio = int(round(mtWin / stStep))
    mtStepRatio = int(round(mtStep / stStep))

    stFeatures = stFeatureExtraction2(signal,Fs, stWin, stStep)

    numOfFeatures = len(stFeatures)

    numOfStatistics = 4

    mtFeatures = []
    # for i in range(numOfStatistics * numOfFeatures + 1):
    for i in range(numOfStatistics * numOfFeatures):
        mtFeatures.append([])

    for i in range(numOfFeatures):  # for each of the short-term features:
        curPos = 0
        N = len(stFeatures[i])
        while (curPos < N):
            N1 = curPos
            N2 = curPos + mtWinRatio
            if N2 > N:
                N2 = N
            curStFeatures = stFeatures[i][N1:N2]

            mtFeatures[i].append(np.mean(curStFeatures))
            mtFeatures[i + numOfFeatures].append(np.std(curStFeatures))
            mtFeatures[i + 2 * numOfFeatures].append(np.max(curStFeatures))
            mtFeatures[i + 3 * numOfFeatures].append(np.min(curStFeatures))
           # lower = np.sort(curStFeatures)[0:int(curStFeatures.shape[0] / 3)]
           # upper = np.sort(curStFeatures)[-int(curStFeatures.shape[0] / 3)::]
           ##    mtFeatures[i + 4 * numOfFeatures].append(np.mean(lower))
            #else:
             #   mtFeatures[i + 4 * numOfFeatures].append(np.mean(curStFeatures))
            #if upper.shape[0] > 0:
             #   mtFeatures[i + 5 * numOfFeatures].append(np.mean(upper))
            #else:
             #   mtFeatures[i + 5 * numOfFeatures].append(np.mean(curStFeatures))
            '''                
            if lower.shape[0]>0:
                mtFeatures[i+6*numOfFeatures].append(np.mean(lower))
            else:
                mtFeatures[i+6*numOfFeatures].append(np.mean(curStFeatures))
            if upper.shape[0]>0:
                mtFeatures[i+7*numOfFeatures].append(np.mean(upper))
            else:
                mtFeatures[i+7*numOfFeatures].append(np.mean(curStFeatures))
            '''
            curPos += mtStepRatio

    return np.array(mtFeatures), stFeatures




def stFeatureExtraction2(signal,Fs, Win, Step):
    """
    This function implements the shor-term windowing process. For each short-term window a set of features is extracted.
    This results to a sequence of feature vectors, stored in a np matrix.

    ARGUMENTS
        signal:       the input signal samples
        Fs:           the sampling freq (in Hz)
        Win:          the short-term window size (in samples)
        Step:         the short-term window step (in samples)
    RETURNS
        stFeatures:   a np array (numOfFeatures x numOfShortTermWindows)
    """

    Win = int(Win)
    Step = int(Step)

    # Signal normalization
    signal = np.double(signal)

    # signal = signal / (2.0 ** 15)
    DC = signal.mean()
    MAX = (np.abs(signal)).max()
    signal = (signal - DC)

    N = len(signal)  # total number of samples
    curPos = 0
    countFrames = 0
    nFFT = Win / 2

    Features_per_window = 13
    numOfTimeSpectralFeatures = Features_per_window * 2 # each fv cointains 14 features from the current window + 14 features from the previous window
    numOfDeltaFeatures = Features_per_window

    totalNumOfFeatures = numOfTimeSpectralFeatures

    stFeatures = []
    stFeaturesDelta = []


    prevFV = np.zeros((totalNumOfFeatures, 1))
    while (curPos + Win - 1 < N):  # for each short-term window until the end of signal
        countFrames += 1
        x = signal[curPos:curPos + Win]  # get current window
        curPos = curPos + Step  # update window position
        X = abs(fft(x))  # get fft magnitude
        X = X[0:int(nFFT)]  # normalize fft
        X = X / len(X)
        if countFrames == 1:
            Xprev = X.copy()  # keep previous fft mag (used in spectral flux)
        curFV = np.zeros((totalNumOfFeatures, 1))
        curFVdelta = np.zeros((numOfDeltaFeatures, 1))

        # signal features
        curFV[0] = np.min(x)
        curFV[1] = np.max(x)
        curFV[2] = np.std(x)
        curFV[3] = np.mean(x)
        # spectral features
        curFV[4] = np.min(X)
        curFV[5] = np.max(X)
        curFV[6] = np.std(X)
        curFV[7] = np.mean(X)
        curFV[8] = stSpectralEntropy(X) 
        curFV[9] = stSpectralFlux(X, Xprev)  # spectral flux
        # zero crossing rate
        curFV[10] = stZCR(x)  
        # energy entropy
        curFV[11] = stEnergyEntropy(x)
        #WAMP
        curFV[12] = WAMP(x)

        #------DELTAS-------#
        # TODO: TEST DELTA
        if countFrames > 1:
            curFV[int(numOfTimeSpectralFeatures / 2)::] = curFV[0:int(numOfTimeSpectralFeatures / 2)] - prevFV[0:int(numOfTimeSpectralFeatures / 2)]
            curFVdelta = curFV[0:int(numOfTimeSpectralFeatures / 2)] - prevFV[0:int(numOfTimeSpectralFeatures / 2)]
        else:
            curFV[int(numOfTimeSpectralFeatures / 2)::] = curFV[0:int(numOfTimeSpectralFeatures / 2)]
            curFVdelta = curFV[0:int(numOfTimeSpectralFeatures / 2)]


        stFeatures.append(curFV)
        stFeaturesDelta.append(curFVdelta)

        prevFV = curFV.copy()
        Xprev = X.copy()

    stFeatures = np.concatenate(stFeatures, 1)
    stFeaturesDelta = np.concatenate(stFeaturesDelta, 1)
   # print"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
   #m print"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    #return stFeaturesDelta
    #sys.exit()
    return stFeatures


def WAMP(x):
    wamp = []
    for i in range(len(x)):
        if i >0:
             if abs(x[i] - x[i-1])>0.0001 : wamp.append(1)
    swamp = sum(wamp)
    #print swamp

    return swamp



def stMADev(X):
    """Compute the Mean absolute deviation"""
    return np.mean(abs(X - np.mean(X)))



def stZCR(frame):
    """Computes zero crossing rate of frame"""
    count = len(frame)
    countZ = np.sum(np.abs(np.diff(np.sign(frame)))) / 2
    return (np.float64(countZ) / np.float64(count - 1.0))



def stEnergyEntropy(frame, numOfShortBlocks=10):
    """Computes entropy of energy"""
    Eol = np.sum(frame ** 2)  # total frame energy
    L = len(frame)
    subWinLength = int(np.floor(L / numOfShortBlocks))
    if L != subWinLength * numOfShortBlocks:
        frame = frame[0:subWinLength * numOfShortBlocks]
    # subWindows is of size [numOfShortBlocks x L]
    subWindows = frame.reshape(subWinLength, numOfShortBlocks, order='F').copy()

    # Compute normalized sub-frame energies:
    s = np.sum(subWindows ** 2, axis=0) / (Eol + eps)

    # Compute entropy of the normalized sub-frame energies:
    Entropy = -np.sum(s * np.log2(s + eps))
    return Entropy



def stSpectralCentroidAndSpread(X, fs):
    """Computes spectral centroid of frame (given abs(FFT))"""
    ind = (np.arange(1, len(X) + 1)) * (fs / (2.0 * len(X)))

    Xt = X.copy()
    Xt = Xt / Xt.max()
    NUM = np.sum(ind * Xt)
    DEN = np.sum(Xt) + eps

    # Centroid:
    C = (NUM / DEN)

    # Spread:
    S = np.sqrt(np.sum(((ind - C) ** 2) * Xt) / DEN)

    # Normalize:
    C = C / (fs / 2.0)
    S = S / (fs / 2.0)

    return (C, S)



def stSpectralEntropy(X, numOfShortBlocks=10):
    """Computes the spectral entropy"""
    L = len(X)  # number of frame samples
    Eol = np.sum(X ** 2)  # total spectral energy

    subWinLength = int(np.floor(L / numOfShortBlocks))  # length of sub-frame
    if L != subWinLength * numOfShortBlocks:
        X = X[0:subWinLength * numOfShortBlocks]

    subWindows = X.reshape(subWinLength, numOfShortBlocks, order='F').copy()  # define sub-frames (using matrix reshape)
    s = np.sum(subWindows ** 2, axis=0) / (Eol + eps)  # compute spectral sub-energies
    En = -np.sum(s * np.log2(s + eps))  # compute spectral entropy

    return En



def stSpectralFlux(X, Xprev):
    """
    Computes the spectral flux feature of the current frame
    ARGUMENTS:
        X:        the abs(fft) of the current frame
        Xpre:        the abs(fft) of the previous frame
    """
    # compute the spectral flux as the sum of square distances:
    sumX = np.sum(X + eps)
    sumPrevX = np.sum(Xprev + eps)
    F = np.sum((X / sumX - Xprev / sumPrevX) ** 2)

    return F


def stSpectralRollOff(X, c, fs):
    """Computes spectral roll-off"""
    totalEnergy = np.sum(X ** 2)
    fftLength = len(X)
    Thres = c * totalEnergy
    # Ffind the spectral rolloff as the frequency position where the respective spectral energy is equal to c*totalEnergy
    CumSum = np.cumsum(X ** 2) + eps
    [a, ] = np.nonzero(CumSum > Thres)
    if len(a) > 0:
        mC = np.float64(a[0]) / (float(fftLength))
    else:
        mC = 0.0
    return (mC)



def createSpectrogramFile(x, Fs, fileName, stWin, stStep,label):
    specgramOr, TimeAxis, FreqAxis = aF.stSpectogram(x, Fs, round(Fs * stWin), round(Fs * stStep), False)
    specgramOr = filter.medfilt2d(specgramOr,5)
    save_path = "medfilt5_label_"+label+'/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    specgram = cv2.resize(specgramOr, (227, 227), interpolation=cv2.INTER_LINEAR)
    im1 = Image.fromarray(np.uint8(matplotlib.cm.jet(specgram) * 255))
    scipy.misc.imsave(save_path+fileName, im1)

