import librosa
import os
import platform
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def load_audio_from_files(paths):
    for index, path in enumerate(paths):
        print("Max of", index, ":", read_audio_file(path));

def read_audio_file(path):
    try:
        y, sr = librosa.load(path)
        max = 0
        for i in y:
            if(max < abs(i)):
                max = i
        return max
    except Exception as e:
        print("An error occured in loading an audio file : \n", e)