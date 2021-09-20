#à faire
# avec Spotify scraper, trouver titre et artiste et cover art, tire album, durée
# télécherger mp3 à partir de recherche sur youtube en 'audio' ssi mp3<durée +10s
# sauvegarder infos dans le fichier mp3, ajouter cover art

#pour les playlists, utiliser spotifyscraper pour obtenir les titres, et faire une boucle

#1
from SpotifyScraper.scraper import Scraper, Request

request = Request().request()
scraper=Scraper(session=request)
track_information = scraper.get_track_url_info(url="http://open.spotify.com/embed/track/6txVOdSbg928oeGhlVUrdK")

print(track_information)