import numpy as np
import math
import var_data as vd
from sklearn.decomposition import PCA
import librosa

def generate_peak_data(signal, sample_rate):
    signal_copy = np.absolute(signal)
    peak_list = ([], [], [], [])
    peak_previous = 0
    index_previous = 0
    samples_before = 0
    samples_after = 0
    peakNum = 0
    song_length = len(signal_copy)
    for index, m in enumerate(signal_copy):
        if index == 0 or index == song_length-1:
            continue
        before = signal_copy[index-1]
        after = signal_copy[index+1]
        if (before < m and after < m and m > 0) or (m < 0 and before > m and after > m):
            peakNum += 1
            if peakNum != 1:
                peak_list[0].append(peak_previous)
                peak_list[1].append(m)
                peak_list[2].append(samples_before)
                peak_list[3].append(samples_after)
            peak_previous = m
            index_previous = index + 1
            samples_before = samples_after
            samples_after = 0
        else:
            samples_after += 1
    del peak_list[0][0]
    del peak_list[1][0]
    del peak_list[2][0]
    del peak_list[3][0]
    return peak_list

def song_bounds(signal, sample_rate):
    data = generate_peak_data(signal, sample_rate)
    return np.asarray([np.amax(data[0]),np.amin(data[0]),np.amax(data[2]),np.amin(data[2])])
            
def mfcc_features(signal,sample_rate):
    return np.asarray(np.mean(librosa.feature.mfcc(y=signal, sr=sample_rate, n_mfcc=20).T,axis=0).tolist())

def pitch_chroma(signal, sample_rate):
    return librosa.feature.chroma_stft(signal, sr=sample_rate)

def probability_analysis(signal, sample_rate):
    return 0
    
data_functions = [mfcc_features, pitch_chroma,song_bounds]

def load_data_from_song(song):
    # Uncompressed
    data = []
    for func in data_functions:
        array = func(song[1], song[0])
        data.append(array)
    if vd.prob_dimension_analysis:
        data.append(probability_analysis(song[1], song[0]))
    return data

def load_data_from_song_uncomp(array):
    # Compressed
    #arraySum = generate_peak_summation(array)
    #return arraySum
    return 0