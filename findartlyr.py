from bs4 import BeautifulSoup
import requests
import time
import lxml
from urllib.request import urlopen
import urllib
from urllib.parse import quote_plus

headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

#urlbase='https://www.google.fr/search?q=bubble+tea&tbm=isch'


def findart(titres):
    urlbase= titres[0][5]
    html = requests.get(urlbase)
    soup = BeautifulSoup(html.content, 'lxml')
    el = soup.findAll(class_="style-scope yt-img-shadow")
    print(el)


findart([['', '', 'n', 'z', 'f', "https://www.youtube.com/results?search_query=chiiild+mahalia+awake+album+audio"]])
