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
    print("The current directory is at :", os.getcwd())
    path = os.getcwd() + input("What folder should music be read in from? : ")
    for audio_format in audio_formats:
        for audio_file in sorted(glob.glob(path + "*." + audio_format)):
            songs_list.append("" + audio_file)
    print("\nFound", len(songs_list), "audio files within the folder!")
    if (input("\nIs this correct? (y/n): ")).lower() == "y":
        songs_data = mst.load_audio_from_files(songs_list)
        #print(len(songs_data[0][1]))
        #print(len(songs_data[1][1]))
        #dt.generate_peak_data2(songs_data[0][1])
        #dt.generate_peak_data2(songs_data[1][1])
        sum_data = dt.load_data_from_songs(songs_data)
        for info in sum_data:
            mst.view_data_array(info[1])
    else:
        print("\nGood day.")
        exit()
    
    
if __name__ == "__main__":
    main()
    
# coophenetic coorelation co-efficient -> for deciding if clustering is good