import typer
import glob
import os
import music_tools as mst
import data_tools as dt
import numpy as np

# Common audio file extensions to look for
audio_formats = ["mp3", "ogg", "wav", "flac", "m4a", "aac", "webm", "opus"]

# Returned by load_songs
songs_list = []
# Returned by get_wave_data_from_songs
songs_data = []
# Summation data from data_tools - structure is [(path1, numpy_array{data}), ..., ...]
sum_data = []

def main():
    length = 9929192
    input_count = 100
    peaksPerSum = (int) (length / input_count)
    print(":", len(range(0, length, peaksPerSum)))
    print("The current directory is at :", os.getcwd())
    path = os.getcwd() + input("What folder should music be read in from? : ")
    for audio_format in audio_formats:
        for audio_file in sorted(glob.glob(path + "*." + audio_format)):
            songs_list.append("" + audio_file)
    print("\nFound", len(songs_list), "audio files within the folder!")
    if (input("\nIs this correct? (y/n): ")).lower() == "y":
        songs_data = mst.load_audio_from_files(songs_list)
        sum_data = dt.load_data_from_songs(songs_data)
    else:
        print("\nGood day.")
        exit()
    
    
if __name__ == "__main__":
    main()