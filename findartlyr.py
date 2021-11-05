import eyed3
import urllib.request

def art(titre)

    audiofile = eyed3.load()
    audiofile.initTag(version=(2, 3, 0))
    audiofile.tag.artist = titre[1]
    audiofile.tag.album = titre[2]
    audiofile.tag.title = titre[0]
    response = urllib.request.urlopen("https://img.youtube.com/vi/{}/mqdefault.jpg".format(titre[5]))
    imagedata = response.read()
    audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
    audiofile.tag.save()