import numpy as np
import math

# Set global variables
input_count = 100
category_count = 10

samples_before = 0
last_peak = 0
sampleDivider = 100.0

currentLevelSum = 0

# Used to store data from generate_peak_data for each song
songs_info = []

def load_data_from_songs(songs_data):
    for info in songs_data:
        array = generate_peak_data(info[0], info[1])
        arraySum = generate_peak_summation(array)
        songs_info.append((info[0], arraySum))
    return songs_info

def generate_peak_data2(song_data):
    count = []
    for index, sample in enumerate(song_data):
        if(index > 200):
            print(count)
            return
        count.append(sample)

def generate_peak_data(song_path, song_data):
    global samples_before
    global last_peak
    # This function is used to gather the data from the waveform of a song
    
    # max will be used to divide all of the peak's values to equalize values between songs
    max = 0
    length = len(song_data)
    # peak_data holds the low and high peak's values of the waveform for further calculations
    peak_data = []
    # loop through all samples in the song
    for index, sample in enumerate(song_data):
        if abs(sample) > max:
            max = (sample)
        sampleB = 0 if index == 0 else song_data[index - 1]
        sampleA = 0 if index + 1 >= length else song_data[index + 1]
        # if the sample before and after are both higher or lower than the current sample,
        # the current sample is a peak within the song's waveform
        if((sampleB < sample and sampleA < sample) or (sampleB > sample and sampleA > sample)):
            # without the -1*, traveling from a low peak to a high peak has the opposite sign
            # sample difference is the distance between the last peak and the current
            sampleDifference = -1 * (last_peak - sample)
            # peak difference is the importance of the peak compared to the other peaks
            # for instance, a sound with a lot of buildup is more important than one with none,
            # therefore if a sound has many samples before it that aren't peaks, multiple the peak's
            # difference value more
            peakDifference = sampleDifference * (1.0 + (samples_before / sampleDivider))
            # add difference and then reset variable values
            peak_data.append(peakDifference)
            last_peak = sample
            samples_before = 0
        else:
            samples_before += 1
    return (np.asarray(peak_data) / max)
            
def generate_peak_summation(song_data):
    global currentLevelSum
    # This function uses the output from generate_peak_data to further condense the data for 
    # optimization during neural network training.
    
    # The main idea behind the algorithm is to split the original dataset into splices, then
    # add the values in these splices together to get a total change in a particular time frame
    
    # These splices are what the neural network will use a training data
    length = len(song_data)
    peaks_final = np.zeros(input_count)
    peaksPerSum = (int) (length / input_count)
    for index, i in enumerate(range(0, length, peaksPerSum)):
        if index >= input_count:
            return peaks_final
        for j in range(0, peaksPerSum, 1):
                currentLevelSum += song_data[i + j]
        peaks_final[index] = currentLevelSum
        currentLevelSum = 0
    return peaks_final