import typer
import glob
import os
import music_tools as mst
import data_tools as dt
import numpy as np
import sys
import var_data as vd
import file_functions as ff
import music_analysis as msa

def initilize_program():
    vd.program_path = sys.path[0]
    ff.create_project_directories(vd.program_path)
    vd.music_files_path = os.getcwd() + input("\nWhat folder should music be read in from? : ")

def main():
    print("The current directory is at :", os.getcwd())
    initilize_program()
    
    # Load all audio file names located in specific directory, save to songs_list
    for audio_format in vd.audio_formats:
        for audio_file in sorted(glob.glob(vd.music_files_path + "*." + audio_format)):
            vd.songs_list.append("" + audio_file)
            
    print("\nFound", len(vd.songs_list), "audio files within the folder!")
    if (input("\nIs this correct? (y/n): ")).lower() == "y":
        mst.load_audio_from_files(vd.songs_list, True)
        #for info in vd.compressed_audio:
            #mst.view_data_array(info)
        msa.train_music_model()
    else:
        print("\nGood day.")
        exit()

if __name__ == "__main__":
    main()
    
# coophenetic coorelation co-efficient -> for deciding if clustering is good