import numpy as np

# storage variables
compressed_audio = []
songs_list = []
array_audio = None

def stretch_func(arr, length=1):
    repetitions = np.round(np.linspace(0,length,arr.shape[0]+1))[1:] - np.round(np.linspace(0,length,arr.shape[0]+1))[:-1]
    repeated = np.repeat(arr, repetitions.astype(np.int))
    return repeated

def convert_list_to_array():
    global array_audio
    names = []
    mel = []
    max_pitch = 0
    pitch = []
    pitch2 = []
    bounds = []
    for info in compressed_audio:
        names.append(info[0])
        mel.append(info[1][0])
        pi2 = (info[1][1]).flatten()
        if max_pitch < len(pi2):
            max_pitch = len(pi2)
        pitch.append(pi2)
        bounds.append(info[1][2])
    names = np.asarray(names)
    mel = np.asarray(mel)
    pitch = np.asarray(pitch)
    for index, i in enumerate(pitch):
        pitch2.append(stretch_func(i, max_pitch))
    bounds = np.asarray(bounds)
    pitch = np.asarray(pitch)
    array_audio = (names, mel, pitch2, bounds)

# settings variables
save_uncompressed = False
audio_formats = ["mp3", "ogg", "wav", "flac", "m4a", "aac", "webm", "opus"]
prob_dimension_analysis = False

# file_functions variables
program_path = ""
music_files_path = ""
audio_data_dir = "audio_data"
data_dirs = ["audio_data/mel", "audio_data/pitch", "audio_data/bounds", "audio_data/prob"]

# data_tools variables
sampleDivider = 400.0
input_count = 2
category_count = 10