import typer
import glob
import os
import music_tools as mst
import data_tools as dt
import numpy as np
import sys
import var_data as vd
import file_functions as ff

# Common audio file extensions to look for
audio_formats = ["mp3", "ogg", "wav", "flac", "m4a", "aac", "webm", "opus"]

# Returned by load_songs
songs_list = []
# Returned by get_wave_data_from_songs
songs_data = []
# Summation data from data_tools - structure is [(path1, numpy_array{data}), ..., ...]
sum_data = []

def initilize_program():
    vd.program_path = sys.path[0]
    ff.create_project_directories(vd.program_path)
    vd.music_files_path = os.getcwd() + input("What folder should music be read in from? : ")

def main():
    print("The current directory is at :", os.getcwd())
    initilize_program()
    
    # Load all audio file names located in specific directory, save to songs_list
    for audio_format in audio_formats:
        for audio_file in sorted(glob.glob(vd.music_files_path + "*." + audio_format)):
            songs_list.append("" + audio_file)
            
    print("\nFound", len(songs_list), "audio files within the folder!")
    if (input("\nIs this correct? (y/n): ")).lower() == "y":
        mst.load_audio_from_files(songs_list)
        for info in vd.compressed_audio:
            mst.view_data_array(info[1])
    else:
        print("\nGood day.")
        exit()

if __name__ == "__main__":
    main()
    
# coophenetic coorelation co-efficient -> for deciding if clustering is good