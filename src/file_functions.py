import os
import var_data as vd
import glob
import numpy as np

def create_project_directories(project_path):
    if os.path.exists(project_path + "/audio_data") == False:
        os.mkdir(project_path + "/audio_data")
    if os.path.exists(project_path + "/" + vd.uncompressed_data_dir) == False:
        os.mkdir(project_path + "/" + vd.uncompressed_data_dir)
    if os.path.exists(project_path + "/" + vd.compressed_data_dir) == False:
        os.mkdir(project_path + "/" + vd.compressed_data_dir)
        
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
    uncomp = ""
    comp = ""
    if os.path.exists(vd.program_path + "/" + vd.compressed_data_dir + "/" + saved_name):
        if os.path.exists(vd.program_path + "/" + vd.uncompressed_data_dir + "/" + saved_name):
            uncomp = vd.program_path + "/" + vd.uncompressed_data_dir + "/" + saved_name
            comp = vd.program_path + "/" + vd.compressed_data_dir + "/" + saved_name
            return (audio_file_name[2], np.load(uncomp), np.load(comp))
        else:
            comp = vd.program_path + "/" + vd.compressed_data_dir + "/" + saved_name
            return (audio_file_name[2], np.array([]), np.load(comp))
    return None
         
def save_data_to_file(data, name, is_compressed):
    # Data must be a numpy array
    path_choice = vd.compressed_data_dir if is_compressed else vd.uncompressed_data_dir
    path_choice = vd.program_path + "/" + path_choice + "/" + name[2] + ".npy"
    if os.path.exists(path_choice):
        os.remove(path_choice)
    np.save(path_choice, data)
    