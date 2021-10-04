from bs4 import BeautifulSoup
import requests
import lxml
from urllib.request import urlopen
from urllib.parse import quote_plus

headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

urlbase='https://www.google.fr/search?q=bubble+tea&tbm=isch'
html_page = requests.get(urlbase, headers=headers)
print(html_page.url)
soup = BeautifulSoup(html_page.content, 'lxml')

img_link = soup.find_all('img', class_='rg_i Q4LuWd')
#full = urlbase+ext

for image in img_link:
    print(image.get('src'))