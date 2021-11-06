import requests
from bs4 import BeautifulSoup
import time

base_url = "http://api.genius.com"
headers = {'Authorization': 'Bearer ykcYOVAnxvrxPJNIObh9OFcuY2Oc0oeP1gZLAZo3lLW6KKUcWoRk_bual0OD-rAC'}


def getlyricsfromname(nom, artiste):
  song_title = nom
  artist_name = artiste.replace(";", " &")
  print(artist_name)

  search_url = base_url + "/search"
  data = {'q': song_title}
  response = requests.get(search_url, params=data, headers=headers)
  json = response.json()
  song_info = None
  for hit in json["response"]["hits"]:
    if hit["result"]["primary_artist"]["name"] == artist_name:
      song_info = hit
      break
  if song_info:
    song_api_path = song_info["result"]["api_path"]
    image = song_info["result"]["header_image_thumbnail_url"]
    return (lyrics_from_song_api_path(song_api_path), image) #song_info["result"]["im"])



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
  try:
    lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
  except AttributeError:
    time.sleep(1)
    lyrics = html.find("div", class_="lyrics").get_text()
  return lyrics
