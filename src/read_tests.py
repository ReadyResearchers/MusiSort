import librosa
import os
import platform

def main():
    print("hello")
    print("", os.getcwd())
    directory = os.getcwd() + "/src/test_songs/Thelema.wav"
    y, sr = librosa.load(directory)
    max = 0
    for i in y:
        if(max < abs(i)):
            max = i
    print("\n", max)
    
    list = []
    for i in range(30):
        list.append(y[i + 200000])
    print(list)
       
if __name__ == "__main__":
    main()