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
import youtube_dl
from pytube import YouTube



def findall(titres):
    for i in range (len(titres)):
      findvid(titres[i])

def findvid(titre):
    search_keyword= remover(titre[0]+'+'+titre[1]+'audio')
    search_keyword= "".join(search_keyword.split())
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])

#https://open.spotify.com/playlist/6iV0C1GGfNmkxH7M3qddl5

def data(file):
  titres = []

  dt = pd.read_csv(file, usecols= ['Track Name','Arist(s) Name'])
  for i in range (len(dt)):
    titres.append([[], []])
    titres[i][0]=dt.loc[i, 'Track Name']
    titres[i][1]=dt.loc[i, 'Arist(s) Name']
  return titres

#print(data('/home/mrnb/Téléchargements/spotlistr-exported-playlist.csv'))

def download(url):

    video = YouTube(url).streams.filter(only_audio=True).first()
  
    # check for destination to save file
    destination = '.'
      
    # download the file
    out_file = video.download(output_path='$HOME')
      
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
      
    # result of success
    print(YouTube(url).title + " has been successfully downloaded.")