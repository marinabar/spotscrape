from main import findvid, data, findall, download, gendownloads, meta
from remover import remover

#findall(data('/home/mrnb/Téléchargements/spotlistr-exported-playlist.csv'))

#download('https://www.youtube.com/watch?v=K58GojV2tz0')
file = '/home/mrnb/Téléchargements/spotlistr-exported-playlist (1).csv'
'''meta(gendownloads(findall(data(file))), file)'''

import eyed3

audiofile = eyed3.load('Chiiild - Awake ft Mahalia (Audio).mp3')
audiofile.initTag()
print(audiofile)
