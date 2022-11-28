import os
import var_data as vd
import glob
import numpy as np

def create_project_directories(project_path):
    if os.path.exists(project_path + "/audio_data") == False:
        os.mkdir(project_path + "/audio_data")
    for dir in vd.data_dirs:
        if os.path.exists(project_path + "/" + dir) == False:
            os.mkdir(project_path + "/" + dir)
        
def get_audio_name_from_path(path):
    file_name = path
    ext = ""
    if file_name.rfind("/") != -1:
        file_name = file_name[file_name.rfind("/")+1 : len(file_name)]
    if file_name.rfind(".") != -1:
        ext = file_name[file_name.rfind(".")+1 : len(file_name)]
        file_name = file_name[0 : file_name.rfind(".")]
    else:
        return None
    return (file_name, ext, (file_name + "-" + ext))
        
def load_local_data_file(path):
    # Parse file name and file extension from file path
    audio_file_name = get_audio_name_from_path(path)
    
    saved_name = audio_file_name[2] + ".npy"
    data = []
    for dir in vd.data_dirs:
        if os.path.exists(vd.program_path + "/" + dir + "/" + saved_name):
            data.append(np.load(vd.program_path + "/" + dir + "/" + saved_name))
        elif dir == "audio_data/prob" and vd.prob_dimension_analysis == False:
            continue
        else:
            return None
    return (audio_file_name[2], data)
         
def save_data_to_file(data, name):
    # Data must be a numpy array
    for index, data_type in enumerate(data):
        path_choice = vd.program_path + "/" + vd.data_dirs[index] + "/" + name[2] + ".npy"
        if os.path.exists(path_choice):
            os.remove(path_choice)
        np.save(path_choice, data_type)
    