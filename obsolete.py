from SpotifyScraper.scraper import Scraper, Request

import eyed3


def playList():
    url = str(input("your playlist url "))
    request = Request().request()
    scraper=Scraper(session=request)
    playlist = scraper.get_playlist_url_info(url=url)

    titres = []

    for i in range(len(playlist['tracks_list'])):
      titres.append([[], []])
      titres[i][0] = playlist['tracks_list'][i]['track_name']
      titres[i][1] = playlist['tracks_list'][i]['track_singer']

    print(titres)
    return titres


'''ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
    }
    if __name__ == "__main__":
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          filenames = url
          ydl.download(filenames)'''


def meta(filenames, csvplaylist):
  
  titre = data(csvplaylist) #load file
  for i in range (len(filenames)):
    print(filenames[i])
    audiofile = eyed3.load(filenames[i])
    print(audiofile)
    audiofile.initTag()
    audiofile.tag.artist = titre[i][0]
    audiofile.tag.album = titre[i][2]
    audiofile.tag.title = titre[i][1]
    audiofile.tag.save()

