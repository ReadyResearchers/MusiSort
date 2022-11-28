import librosa
import os
import platform
import sys
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time
import var_data as vd
import file_functions as ff
import data_tools as dt
import gc

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#def load_audio_from_files(paths): # Deprecated --
#    audio_list = []
#    for index, path in enumerate(paths):
#        audio_list.append((path, read_audio_file(path)[0]));
#        time.sleep(1)
#    return audio_list

def load_audio_from_files(paths, skip_new_load):
    total = len(paths)
    for index, path in enumerate(paths):
        if index % 50 == 0:
            print("\nCompleted", index, "out of", total, "songs.")
        loaded_data = ff.load_local_data_file(path)
        
        # No numpy file was found for the song retrieved
        if loaded_data == None and skip_new_load == False:
            # Get the file name of the song and audio data
            audio_name = ff.get_audio_name_from_path(path)
            audio_read = read_audio_file(path);
            # If audio data failed to load, skip to next song
            if audio_read == None: 
                continue
            audio_full = audio_read[0]
            sample_rate = audio_read[1]
            # Parse audio data with data tools methods
            audio_data = dt.load_data_from_song((sample_rate, audio_full))
            # Save parsed data to numpy files for future use
            ff.save_data_to_file(audio_data, audio_name)
            # Add compressed audio data to global list in var_data : (numpy_file_name, data)
            vd.compressed_audio.append((audio_name[2], audio_data))
            # Clear large sized variables for memory
            audio_data = None
            audio_full = None
        elif loaded_data != None:
            # Add compressed audio data to global list in var_data : (numpy_file_name, data)
            title = loaded_data[0]
            data = loaded_data[1]
            vd.compressed_audio.append((title, data))  

        # Sleep program to lessen process strain
        if (loaded_data == None and skip_new_load == False) or index % 25 == 0:
            time.sleep(1)
            if (loaded_data == None and skip_new_load == False) and index % 10 == 0:
                gc.collect()
    return 1

def read_audio_file(path):
    try:
        info = librosa.load(path)
        return info
    except Exception as e:
        print("An error occured in loading an audio file : \n", repr(e))
        return None
        
def view_data_array(info):
    val = 0
    print("\n\n", info[0], "\n", info[1], "\n\n")