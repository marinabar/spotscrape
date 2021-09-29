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

import eyed3


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
      urlsvideos.append(findvid(titres[i]))

    return urlsvideos


def findvid(titre):
  #given a song title, find its corresponding url
    search_keyword= (remover(str(titre[0]) + str(titre[1])+'album audio'))
    print(search_keyword)
    search_keyword= "".join(search_keyword.split())
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    return ("https://www.youtube.com/watch?v=" + video_ids[0])

#https://open.spotify.com/playlist/6iV0C1GGfNmkxH7M3qddl5


#print(data('/home/mrnb/Téléchargements/spotlistr-exported-playlist.csv'))

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
    os.rename(out_file, new_file)
      
    # result of success
    print(YouTube(url).title + " has been successfully downloaded.")
    return new_file

def gendownloads(urlvideos):
  #loop over all urls in list and download each one of them

    filenames = []
    for i in range (len(urlvideos)):
      filenames.append(download(urlvideos[i]))

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
    audiofile.tag.save()

