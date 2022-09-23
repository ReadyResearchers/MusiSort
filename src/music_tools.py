import librosa
import os
import platform
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def load_audio_from_files(paths):
    audio_list = []
    for index, path in enumerate(paths):
        audio_list.append((path, read_audio_file(path)[0]));
    return audio_list

def read_audio_file(path):
    try:
        info = librosa.load(path)
        return info
    except Exception as e:
        print("An error occured in loading an audio file : \n", e)
        
def view_data_array(array):
    val = 0
    print("\n\n", array, "\n\n")
    #plt.plot(array, np.zeros_like(array) + val, 'x')
    #plt.show()