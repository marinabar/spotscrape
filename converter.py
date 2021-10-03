from moviepy.editor import *
import os

def conv (mp4, mp3):
    audioclip = AudioFileClip(mp4)
    audioclip.write_audiofile(mp3)
    audioclip.close()
    dir_name = "/home/mrnb/Bureau/code/2021/spotscrape/tele/"
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".mp4"):
            os.remove(os.path.join(dir_name, item))