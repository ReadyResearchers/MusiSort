import numpy as np
import matplotlib.pyplot as plt
from musisort import classification_manager, file_manager, global_variables
import random

def delete_section(x, perc):
    if random.randint(0, 99) < perc:
        return 0
    return x

def delete_percent(array, percent):
    array_copy = array
    size = len(array)
    iter = 0 if percent == 0 else (10/percent)*10
    count = iter
    for index, val in enumerate(array):
        if index < count and (index + 1) >= count:
            count = count + iter
            array_copy[index] = 0
    return array_copy

def reduce_waveform(waveform, percentage):
    # 0 = 0% change, 100 = silent song
    #delete_v = np.vectorize(delete_section)
    #array2 = delete_v(waveform, percentage)
    array2 = delete_percent(waveform, percentage)
    return array2
    
def debug(classification_info):
    # (song_values, final_combined_clusters, songs)
    #  labels     , cluster coords,        , song paths
    songs = classification_info[2]
    data_types_enabled = []
    
    for data_type in global_variables.data_types_enabled.keys():
        if global_variables.data_types_enabled[data_type]:
            data_types_enabled.append(data_type)

    #loaded_song = file_manager.load_song_data_file(data_type, song[0], song[1])
    print(classification_info)