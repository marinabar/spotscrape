from mutagen.easyid3 import EasyID3
import mutagen

filepath = "/home/mrnb/Bureau/code/2021/spotscrape/tele/Chiiild - Awake ft Mahalia (Audio).mp3"
'''try :
    audio = EasyID3(filepath)
except mutagen.id3.ID3NoHeaderError:
    audio = mutagen.File(filepath, easy=True)
    audio.add_tags()

audio["title"] = u"Awake ft Mahalia"
audio.save()'''

from mutagen.id3 import ID3NoHeaderError

from mutagen.id3 import Encoding, PictureType
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK, USLT

# Read the ID3 tag or create one if not present
try: 
    tags = ID3(filepath)
except ID3NoHeaderError:
    tags = mutagen.File(filepath)
    tags.add_tags()

title = 'Awake ft. Mahalia'
lyrics = ""

tags["TIT2"] = TIT2(encoding=3, text=title)
tags["TALB"] = TALB(encoding=3, text=u'mutagen Album Name')
tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'mutagen comment')
tags["TPE1"] = TPE1(encoding=3, text=u'mutagen Artist')
#tags["TDRC"] = TDRC(encoding=3, text=u'')
uslt_output = USLT(encoding=3, lang=u'eng', desc=u'desc', text=lyrics)
#tags["USLT::'eng'"] = uslt_output
tags["TRCK"] = TRCK(encoding=3, text=u'track_number')

tags.save(filepath)