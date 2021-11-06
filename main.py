from remover import remover
from findlyrics import getlyricsfromname

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
    urlsvideos=[]
    for i in range (len(titres)):
      titres[i].append([])
      titres[i].append([])
      titres[i][4], titres[i][5] = findvid(titres[i])
  
    return titres


def findvid(titre):
  #given a song title, find its corresponding url
    search_keyword= (remover(str(titre[0]) + str(titre[1])+'album audio'))
    print("Searching for " + search_keyword)
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

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener() # otherwise can't open url with urllib


def meta(titres):
  #print(titres)
  token = str(input("Please paste your token "))
  for titre in titres:
    audiofile = eyed3.load(titre[6])
    audiofile.initTag()
    audiofile.tag.artist = titre[1]
    audiofile.tag.album = titre[2]
    audiofile.tag.title = titre[0]

    lyrics, image = getlyricsfromname(titre[0], titre[1], token)
    audiofile.tag.lyrics.set(lyrics)

    response = opener.open(image)  
    imagedata = response.read()
    if image.split(".")[4] == 'png' :
      type_ = 'image/png' # gets the extension
    else:
      type_ = "image/jpeg"
    audiofile.tag.images.set(3, imagedata, type_, description=u"album art")


    audiofile.tag.save(encoding='utf-8')