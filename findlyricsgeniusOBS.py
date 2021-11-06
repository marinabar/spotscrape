import requests
from bs4 import BeautifulSoup
import time

base_url = "http://api.genius.com"


def getlyricsfromname(nom, artiste, token):

  headers = {'Authorization': ('Bearer '+token)}

  song_title = nom.split("(")[0]
  artist_name = artiste.replace(";", " &").strip()
  print(artist_name.split("&")[0], song_title)
  query = song_title + " "+ artist_name.split("&")[0]
  print (query)

  search_url = base_url + "/search"
  data = {'q': query}
  response = requests.get(search_url, params=data, headers=headers)
  json = response.json()
  song_info = None
  for hit in json["response"]["hits"]:
    print(hit)
    if hit["result"]["primary_artist"]["name"] == artist_name:
      song_info = hit
      break
  if song_info:
    song_api_path = song_info["result"]["api_path"]
    print(song_api_path)
    image = song_info["result"]["header_image_thumbnail_url"]
    print(image)
    return (lyrics_from_song_api_path(song_api_path, headers), image) #song_info["result"]["im"])



def lyrics_from_song_api_path(song_api_path, headers):
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
  print(html)
  #at least Genius is nice and has a tag called 'lyrics'!
  try:
    lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
  except AttributeError:
    time.sleep(3)
    lyrics = html.find("div", class_="lyrics").get_text()
  #print (lyrics)
  return lyrics
