import requests
from googley import getlyricsgoogle
from bs4 import BeautifulSoup

def getlyrics(titre):
    artist1 = titre[1].strip() #remove whitespaces around
    if artist1 == 'NCT 127' or artist1 == 'NCT DREAM':
        artist1 = 'NCT' #handle with care <3
    artist1 = artist1.replace(" ", "+").lower() # make it search friendly

    song = ''.join((titre[0].split('(')[0])).strip() # only take the part without the parenthesis
    song = song.replace(" ", "+") # same around here

    queryurl = ("https://search.azlyrics.com/search.php?q="+artist1+"+"+song).lower()
    print(queryurl)


    r= requests.get(queryurl, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"})
    soup = BeautifulSoup(r.content, "html.parser")
    try:
        lyricurl = soup.find("td").find("a")["href"]
        print(lyricurl) # get lyrics link

        return getlyrfromurl(lyricurl)

    except AttributeError:
        print("Getting lyrics from Google...")
        return getlyricsgoogle(titre)



def getlyrfromurl(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    lyric = soup.select_one(".ringtone ~ div").get_text(separator="\n") # at least they're all in the same tag...

    return lyric
