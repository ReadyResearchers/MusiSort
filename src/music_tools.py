import librosa
import os
import platform
import sys

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