import requests

base_url = "http://api.genius.com"


def artfromsong(nom, artiste, token):

  headers = {'Authorization': ('Bearer '+token)}

  song_title = nom.split("(")[0]
  artist_name = artiste.replace(";", " &").strip()
  query = song_title + " "+ artist_name.split("&")[0]

  search_url = base_url + "/search"
  data = {'q': query}
  response = requests.get(search_url, params=data, headers=headers)
  json = response.json()
  song_info = None
  for hit in json["response"]["hits"]:
    if hit["result"]["primary_artist"]["name"] == artist_name:
      song_info = hit
      break
  if song_info:
    image = song_info["result"]["header_image_thumbnail_url"]
    print(image)
    return (image) 

#artfromsong("Je te laisserai des mots", "Patrick Watson", "KOl3mg2btk9MDpm3QBdeeB3IUkMjo2BUS1DtQkG5AO1KdP2b1YRmXJQvPF0BGUOy")