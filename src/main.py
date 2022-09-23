import typer

# Returned by load_songs
songs_list = []
# Returned by get_wave_data_from_songs
songs_data = []

def main(path: str):
    print("path chosen :", path)
    
    
if __name__ == "__main__":
    typer.run(main)

//def load_songs(folder_path_to_songs):
    songs_list = ["./frog.mp3", "./cat.mp3"];
    
//def get_wavedata_from_songs():
    for song in songs_list:
        array = {200, 3, 20, 71, 23, 8, 1}
        songs_data.append((song, array))
