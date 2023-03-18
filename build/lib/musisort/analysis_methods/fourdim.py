"""
"""

import numpy as np

f_v = None

def create_grid(arrays):
    grid = np.asarray([1])
    for array in arrays:
        grid = np.multiply.outer(grid, array)
    grid = grid / grid.sum()
    return np.squeeze(grid)

def get_peaks(song_waveform):
    peaks = [] # distance (frequency), difference (amplitude)
    length = song_waveform.size
    previous_peak_time = -1
    previous_peak_amplitude = -1
    for index in range(1, length-1):
        sample = song_waveform[index]
        if song_waveform[index-1] < sample and sample > song_waveform[index+1]:
            if previous_peak_time != -1:
                distance = abs(previous_peak_time - index)
                difference = abs(previous_peak_amplitude - sample)
                peaks.append([distance, difference])
            previous_peak_time = index
            previous_peak_amplitude = sample
    return np.asarray(peaks)

def function(x, n, upper):
    max = x if x >= n else n
    min = n if x >= n else x
    exponent = upper + (upper * -1 * (min / max))
    return x + ((n-x) * (1 - (1/((abs(n-x)+1)**(exponent)))))

def get_centered_mean(data):
    n = np.median(data)
    upper = 1/2
    return np.mean(f_v(data, n, upper))

def analyze(song_waveform, song_info):
    global f_v
    f_v = np.vectorize(function)
    split_count = 10
    song_data = song_waveform[0]
    min_value = np.min(song_data)
    if min_value < 0:
        song_data = song_data + abs(min_value)
    song_peaks = np.array_split(get_peaks(song_data), split_count)
    distances_mean = []
    differences_mean = []
    distances_max = []
    differences_max = []
    for i in range(split_count):
        current_splice = song_peaks[i]
        distances = current_splice[:, 0]
        differences = current_splice[:, 1]
        distances_mean.append(get_centered_mean(distances))
        differences_mean.append(get_centered_mean(differences))
        distances_max.append(np.max(distances))
        differences_max.append(np.max(differences))
    arrays = (np.asarray(distances_mean),np.asarray(differences_mean),\
        np.asarray(distances_max),np.asarray(differences_max))
    return np.ravel(create_grid(arrays))