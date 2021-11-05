#crops downloaded album art to basic format
from PIL import Image
import urllib.request
import eyed3
import os


def getart(titre):
    imgURL = "https://img.youtube.com/vi/{}/mqdefault.jpg".format(titre[5]) #download from youtube thumbnail
    path = "art.jpg"
    urllib.request.urlretrieve(imgURL, path) # get request
    img = Image.open(path)
    area = (70, 0, 250, 180) #each img has the same area
    image = img.crop(area)
    image.save(path, format="JPEG", optimize=True) #save image

    audiofile.tag.images.set(3, open(path, 'rb').read(), 'image/jpeg')
    audiofile.tag.save()