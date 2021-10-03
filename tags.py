from mutagen.easyid3 import EasyID3
import mutagen

filepath = "/home/mrnb/Bureau/code/2021/spotscrape/Chiiild - Awake ft Mahalia (Audio).mp3"
try :
    audio = EasyID3(filepath)
except mutagen.id3.ID3NoHeaderError:
    audio = mutagen.File(filepath, easy=True)
    audio.add_tags()

audio["title"] = u"Awake ft Mahalia"
audio.save()