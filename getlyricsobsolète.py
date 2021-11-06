def getlyricsurl(titre):
    artist1, artist2 = titre[1].split(';')
    artist1 = (''.join(artist1).split())[0]
    print(artist1)
    artist2 = (''.join(artist2).split())[0]
    song = (''.join((titre[0].split('(')[0]).split()))
    url = ("https://www.azlyrics.com/lyrics/"+artist1+"/"+song+".html").lower()
    
    return url