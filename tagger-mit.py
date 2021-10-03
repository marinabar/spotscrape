from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

filepath = "/home/mrnb/Bureau/code/2021/spotscrape/tele/Chiiild - Awake ft Mahalia (Audio).mp3"

'''mp3 = MP3File(filepath)
mp3.album = 'some title..'
mp3.title = 'some title..'
mp3.artist = 'some title..'
mp3.save()'''

import eyed3

audiofile = eyed3.load(filepath)
audiofile.initTag()
audiofile.tag.artist = 'Chiild'
audiofile.tag.save()