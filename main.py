#à faire
# avec Spotify scraper, trouver titre et artiste et cover art, tire album, durée
# télécherger mp3 à partir de recherche sur youtube en 'audio' ssi mp3<durée +10s
# sauvegarder infos dans le fichier mp3, ajouter cover art

#pour les playlists, utiliser spotifyscraper pour obtenir les titres, et faire une boucle

#1
from SpotifyScraper.scraper import Scraper, Request

from remover import remover

import urllib.request

import pandas as pd
import re

import sys
import youtube_dl


'''def playList():
    url = str(input("your playlist url "))
    request = Request().request()
    scraper=Scraper(session=request)
    playlist = scraper.get_playlist_url_info(url=url)

    titres = []

    for i in range(len(playlist['tracks_list'])):
      titres.append([[], []])
      titres[i][0] = playlist['tracks_list'][i]['track_name']
      titres[i][1] = playlist['tracks_list'][i]['track_singer']

    print(titres)
    return titres'''

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

print(data('/home/mrnb/Téléchargements/spotlistr-exported-playlist.csv'))

def download(url):
    ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
    }
    if __name__ == "__main__":
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          filenames = url
          ydl.download(filenames)