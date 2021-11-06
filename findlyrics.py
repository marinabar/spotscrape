'''def getlyricsurl(titre):
    artist1, artist2 = titre[1].split(';')
    artist1 = (''.join(artist1).split())[0]
    print(artist1)
    artist2 = (''.join(artist2).split())[0]
    song = (''.join((titre[0].split('(')[0]).split()))
    url = ("https://www.azlyrics.com/lyrics/"+artist1+"/"+song+".html").lower()
    
    return url


print(getlyricsurl([' Awake (with Mahalia) ', 'Chiiild; Mahalia ', ' Awake ', ' 00:03:48']))'''




import requests
from bs4 import BeautifulSoup
import time

base_url = "http://api.genius.com"
headers = {'Authorization': 'Bearer ykcYOVAnxvrxPJNIObh9OFcuY2Oc0oeP1gZLAZo3lLW6KKUcWoRk_bual0OD-rAC'}

song_title = "Lake Song"
artist_name = "The Decemberists"

def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  #gotta go regular html scraping... come on Genius
  page_url = "http://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  #remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  #at least Genius is nice and has a tag called 'lyrics'!
  lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
  return lyrics

if __name__ == "__main__":
  search_url = base_url + "/search"
  data = {'q': song_title}
  response = requests.get(search_url, params=data, headers=headers)
  json = response.json()
  song_info = None
  print(json)
  for hit in json["response"]["hits"]:
    if hit["result"]["primary_artist"]["name"] == artist_name:
      song_info = hit
      break
  if song_info:
    song_api_path = song_info["result"]["api_path"]
    print (lyrics_from_song_api_path(song_api_path))