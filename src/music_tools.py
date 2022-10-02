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

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#def load_audio_from_files(paths): # Deprecated --
#    audio_list = []
#    for index, path in enumerate(paths):
#        audio_list.append((path, read_audio_file(path)[0]));
#        time.sleep(1)
#    return audio_list

def load_audio_from_files(paths):
    for index, path in enumerate(paths):
        loaded_data = ff.load_local_data_file(path)
        
        # No numpy file was found for the song retrieved
        if loaded_data == None:
            # Get the file name of the song and audio data
            audio_name = ff.get_audio_name_from_path(path)
            print(path)
            audio_read = read_audio_file(path);
            # If audio data failed to load, skip to next song
            if audio_read == None: 
                continue
            audio_full = audio_read[0]
            # Parse audio data with data tools methods
            audio_data = dt.load_data_from_song((path, audio_full))
            # Save parsed data to numpy files for future use
            if vd.save_uncompressed:
                ff.save_data_to_file(audio_data[0], audio_name, False)
            ff.save_data_to_file(audio_data[1], audio_name, True)
            # Add compressed audio data to global list in var_data : (numpy_file_name, data)
            vd.compressed_audio.append((audio_name[0], audio_data[1]))
            # Clear large sized variables for memory
            audio_data = None
            audio_full = None
        else:
            # Add compressed audio data to global list in var_data : (numpy_file_name, data)
            vd.compressed_audio.append((loaded_data[0], loaded_data[2]))  

        # Sleep program to lessen process strain
        time.sleep(1)
    return 1

def read_audio_file(path):
    try:
        info = librosa.load(path)
        return info
    except Exception as e:
        print("An error occured in loading an audio file : \n", repr(e))
        return None
        
def view_data_array(array):
    val = 0
    print("\n\n", array, "\n\n")