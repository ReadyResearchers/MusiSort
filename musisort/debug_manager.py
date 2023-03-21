import numpy as np
import matplotlib.pyplot as plt
from musisort import analysis_manager, classification_manager, file_manager, global_variables
import random
import os
import gc
import time
from progress.bar import Bar

def delete_section(x, perc):
    if random.randint(0, 99) < perc:
        return 0
    return x

def delete_percent(array, percent):
    changed = 0
    array_copy = np.copy(array)
    size = len(array)
    iter = 0 if percent == 0 else (10/percent)*10
    count = iter
    for index, val in enumerate(array):
        if index < count and (index + 1) >= count:
            changed = changed + 1
            count = count + iter
            array_copy[index] = 0
    return array_copy

def reduce_waveform(waveform, percentage):
    # 0 = 0% change, 100 = silent song
    #delete_v = np.vectorize(delete_section)
    #array2 = delete_v(waveform, percentage)
    array2 = delete_percent(waveform, percentage)
    return array2
    
def debug():
    # -> Make debug folder similar to all folder
    # -> Make new analyze_song in analysis_manager that just takes a waveform and song name info
    # Read single song in folder - if more than one, stop, print error
    songs = file_manager.get_songs("debug")
    if songs == None:
        exit()
    if len(songs) > 1 or len(songs) <= 0:
        print("Error! Only one song can be in the debug list at a time!")
        print("Detected", len(songs), "total songs... Cancelling Debug.")
        exit()
    # load song waveform
    song_path = os.path.join(file_manager.debug_song_list_dir, file_manager.list_song_folder, (songs[0][0] + "." + songs[0][1]))
    loaded_song_waveform = analysis_manager.load_song_waveform(song_path)
    # loop through x times (percentage_iterations) creating new waveform with percentage removed
    bar = Bar('Generating Debug Data', max=(global_variables.debug_remove_iterations-global_variables.debug_iteration_minus))
    
    for iteration in range(1, global_variables.debug_remove_iterations+1-global_variables.debug_iteration_minus, 1):
        percent = int(100/global_variables.debug_remove_iterations) * iteration
        modified_song_name = songs[0][0] + "debug" + str(percent)
        modified_song_waveform = (delete_percent(loaded_song_waveform[0], percent), loaded_song_waveform[1])
        #print("\n", percent, " - ", len(modified_song_waveform[0]), ":" , np.shape(modified_song_waveform[0]), " , " ,len(loaded_song_waveform[0]), ":" , np.shape(loaded_song_waveform[0]))
        # call analyze_song_waveform in analysis_manager with modified waveform
        analysis_manager.analyze_song_waveform(modified_song_name, songs[0][1], modified_song_waveform)
        # song name should be called "<original_song_name>debug<percentage>-flac"
        modified_song_waveform = None
        bar.next()
        gc.collect()
        time.sleep(1)
            
    bar.finish()
    print("\n")
    # -> Make classify load these songs if debug set to True
    classification_info = classification_manager.classify_songs("debug", 2, True)
    print("\nClassification Info Condensed: \n", classification_info)