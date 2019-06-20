from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import os
music_folder=os.path.join('D:','Music')
all_files=os.listdir(music_folder)
for file in all_files:
    print(file)
    if file[-4:] != '.mp3':
        continue
    mp3 = MP3File(music_folder+"\\"+file)
    mp3.set_version(VERSION_2)
    name=mp3.song+".mp3"
    old=os.path.join(music_folder,file)
    new=os.path.join(music_folder,name)
    os.rename(old,new)
