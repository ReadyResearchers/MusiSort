# AutoMusicSort
A tool used to automatically sort lists of music into similar categories.

# Description

AutoMusicSort is a tool being developed to collect music and put them into similar groups or clusters based on their waveform.  The program uses artifical intelligence to check similarities and differences between the different songs.  The main goal of the project is to create a tool which removes the need to manually sort music into different genres as this can be quite a difficult task.  

**Current Project Goals:**

[🏗️] Develop the algorithm to sort songs into categories.

[❌] Optimize the algorithms used to sort songs for faster completion.

[❌] Create a more user friendly terminal interface for easier usage.

[❌] Develop a GUI for more interactivity with the program.

(🏗️ : in progress , ❌ : not started yet , ✅ : completed)

# Information

It is recommended to use wav files when running the program as it provides improved performance.

**Current Dependencies Needed:**

- Typer : pip install "typer[all]"
- Librosa : pip install Librosa
- NumPy : pip install numpy
- ffmpeg : pip install ffmpeg

**Run command:**

`python ./src/main.py "folder_path_to_audio_files"`