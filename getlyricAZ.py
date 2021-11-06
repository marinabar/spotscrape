import requests
from bs4 import BeautifulSoup

def getlyrics(titre):
    artist1 = titre[1].split(';')[0].strip()
    artist1 = artist1.replace(" ", "+").lower()
    #print(artist1)
    song = ''.join((titre[0].split('(')[0])).strip()
    song = song.replace(" ", "+")
    #print(song)

    queryurl = ("https://search.azlyrics.com/search.php?q="+artist1+"+"+song).lower()
    print(queryurl)

    soup = BeautifulSoup(requests.get(queryurl).content, "html.parser")
    #print(soup)
    try:
        lyricurl = soup.find("td").find("a")["href"]
        print(lyricurl)

        return getlyrfromurl(lyricurl)

    except AttributeError:
        print("No lyrics for ", titre[0])



def getlyrfromurl(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    lyric = soup.select_one(".ringtone ~ div").get_text(separator="\n")

    return lyric

#getlyricsurl(["Awake (with Mahalia)", "Chiiild; Mahalia"])
