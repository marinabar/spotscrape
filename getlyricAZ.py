import requests
import random
from bs4 import BeautifulSoup


proxies_list = ["66.23.232.84", "159.197.128.163", "20.186.110.157", "64.235.204.107", "51.195.76.214", "137.164.95.15", "52.183.8.192"]
# update list from free-proxy -> all with the same port and all https !!!

def getlyrics(titre):
    artist1 = titre[1].strip() #remove whitespaces around
    if artist1 == 'NCT 127' or artist1 == 'NCT DREAM':
        artist1 = 'NCT' #handle with care <3
    artist1 = artist1.replace(" ", "+").lower() # make it search friendly

    song = ''.join((titre[0].split('(')[0])).strip() # only take the part without the parenthesis
    song = song.replace(" ", "+") # same around here

    queryurl = ("https://search.azlyrics.com/search.php?q="+artist1+"+"+song).lower()
    print(queryurl)

    proxies = {
    'http': "https://"+ random.choice(proxies_list) + ":3128"
    } # use diferent ip each time

    r = requests.get(queryurl, proxies=proxies)

    soup = BeautifulSoup(r.content, "html.parser")
    try:
        lyricurl = soup.find("td").find("a")["href"]
        print(lyricurl) # get lyrics link

        return getlyrfromurl(lyricurl)

    except AttributeError:
        print("No lyrics for ", titre[0])



def getlyrfromurl(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    lyric = soup.select_one(".ringtone ~ div").get_text(separator="\n") # at least they're all in the same tag...

    return lyric
