from remover import remover

import urllib.request

import pandas as pd
import re

import os, sys
from pytube import YouTube

from converter import conv

import eyed3
from PIL import Image
#from findartlyr import findart

def data(file):
  #given a csv file, output a list with each track as a list of its title, length, album and artist
  titres = []

  dt = pd.read_csv(file)
  for i in range (len(dt)):
    titres.append([[], [], [], []])
    titres[i][0]=dt.loc[i, 'Track Name']
    titres[i][1]=dt.loc[i, 'Arist(s) Name']
    titres[i][2]=dt.loc[i, 'Album Name']
    titres[i][3]=dt.loc[i, 'Length']
    
  return titres


def findall(titres):
  #for a given list, find all youtube urls
    print (titres)
    urlsvideos=[]
    for i in range (len(titres)):
      titres[i].append([])
      titres[i].append([])
      titres[i][4], titres[i][5] = findvid(titres[i])
  
    return titres


def findvid(titre):
  #given a song title, find its corresponding url
    search_keyword= (remover(str(titre[0]) + str(titre[1])+'album audio'))
    print(search_keyword)
    search_keyword= "".join(search_keyword.split())
    url = "https://www.youtube.com/results?search_query=" + search_keyword
    html = urllib.request.urlopen(url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    return ("https://www.youtube.com/watch?v=" + video_ids[0], video_ids[0])

def download(url):
  #download mp3 given a youtube url
    video = YouTube(url).streams.filter(only_audio=True).first()
  
    # check for destination to save file
    destination = 'tele'
      
    # download the file
    out_file = video.download(output_path=destination)
      
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    conv(out_file, new_file)
      
    # result of success
    print(YouTube(url).title + " has been successfully downloaded.")
    return new_file


def gendownloads(titres):
  #loop over all urls in list and download each one of them

    filenames = []
    for i in range (len(titres)):
      titres[i].append(download(titres[i][4]))

    #print(filenames)

    return titres


def meta(titres):
  #print(titres)

  for titre in titres:
    audiofile = eyed3.load(titre[6])
    audiofile.initTag()
    audiofile.tag.artist = titre[1]
    audiofile.tag.album = titre[2]
    audiofile.tag.title = titre[0]

    imgURL = "https://img.youtube.com/vi/{}/mqdefault.jpg".format(titre[5]) #download from youtube thumbnail
    path = "art.jpg"
    urllib.request.urlretrieve(imgURL, path) # get request
    img = Image.open(path)
    area = (70, 0, 250, 180) #each img has the same area
    image = img.crop(area)
    image.save(path, format="JPEG", optimize=True) #save image
    audiofile.tag.images.set(3, open(path, 'rb').read(), 'image/jpeg')

    audiofile.tag.save(encoding='utf-8')
  
  os.remove(path)