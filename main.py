#à faire
# avec Spotify scraper, trouver titre et artiste et cover art, tire album, durée
# télécherger mp3 à partir de recherche sur youtube en 'audio' ssi mp3<durée +10s
# sauvegarder infos dans le fichier mp3, ajouter cover art

#pour les playlists, utiliser spotifyscraper pour obtenir les titres, et faire une boucle

#1

from remover import remover

import urllib.request

import pandas as pd
import re

import os, sys
from pytube import YouTube

from converter import conv

import eyed3
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
      titres[i].append([], [])
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


def gendownloads(urlvideos):
  #loop over all urls in list and download each one of them

    filenames = []
    for i in range (len(urlvideos)):
      filenames.append(download(urlvideos[i][4]))

    print(filenames)

    return filenames


def meta(filenames, csvplaylist):
  
  titre = data(csvplaylist) #load file
  for i in range (len(filenames)):
    print(filenames[i])
    audiofile = eyed3.load(filenames[i])
    print(audiofile)
    audiofile.initTag()
    audiofile.tag.artist = titre[i][0]
    audiofile.tag.album = titre[i][2]
    audiofile.tag.title = titre[i][1]
    audiofile.tag.images.set(type_=3, img_data=None, mime_type=None, description=u"album art", img_url=u"https://img.youtube.com/vi//mqdefault.jpg")
    #audiofile.tag.images.set(type_=3, img_data=None, mime_type=None, description=u"", img_url=findart(titre[i][1], titre[i][2]))
    audiofile.tag.save()