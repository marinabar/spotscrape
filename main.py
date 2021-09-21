#à faire
# avec Spotify scraper, trouver titre et artiste et cover art, tire album, durée
# télécherger mp3 à partir de recherche sur youtube en 'audio' ssi mp3<durée +10s
# sauvegarder infos dans le fichier mp3, ajouter cover art

#pour les playlists, utiliser spotifyscraper pour obtenir les titres, et faire une boucle

#1
from SpotifyScraper.scraper import Scraper, Request
import urllib.request
import re

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

search_keyword= titres[0][0]+'+'+titres[0][1]
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])


#https://open.spotify.com/playlist/6iV0C1GGfNmkxH7M3qddl5