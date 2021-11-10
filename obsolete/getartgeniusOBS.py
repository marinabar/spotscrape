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

# add to main code if you want to use Genius API for art 

    #if image.split(".")[4] == 'png' :
      #type_ = 'image/png' # gets the extension
    #else:
      #type_ = "image/jpeg"
    #only for genius api art
