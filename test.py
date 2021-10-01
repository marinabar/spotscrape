from main import findvid, data, findall, download, gendownloads, meta
from remover import remover

#findall(data('/home/mrnb/Téléchargements/spotlistr-exported-playlist.csv'))

#download('https://www.youtube.com/watch?v=K58GojV2tz0')
file = '/home/mrnb/Téléchargements/spotlistr-exported-playlist (1).csv'
'''meta(gendownloads(findall(data(file))), file)'''

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
