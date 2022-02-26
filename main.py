from remover import nostuff, remover
from getlyricAZ import getlyrics

import urllib.request

import pandas as pd
import re

import os
from pytube import YouTube

from moviepy.editor import AudioFileClip
import os

import eyed3



def rem(word):
  normal = (re.sub("AC0", "", word)).replace("+", "").replace("-", "")
  return normal


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener() # otherwise can't open url with urllib




class Spotscrape:
  def __init__(self):
    self.titres = []
    self.lyrics = []
    self.urls= []
    self.filenames=[]
  
  def getdata(self, data):
    dt = pd.read_csv(data, quotechar='"', encoding="utf-16")
    #dt = pd.read_csv(file)
    for i in range (len(dt)):
      self.titres.append([[], [], [], [], []])
      self.titres[i][0]=dt.loc[i, 'Track Name']
      self.titres[i][1]=dt.loc[i, 'Album Artist Name(s)']
      self.titres[i][2]=dt.loc[i, 'Album Name']
      self.titres[i][3]=dt.loc[i, 'Album Image URL']
      self.titres[i][4]=dt.loc[i, 'Album Release Date']
  
  def findall(self):
  #for a given list, find all youtube urls
    for i in range (len(self.titres)):
      self.titres[i].append([])
      self.titres[i][5] = self.findvid(self.titres[i])


  def findvid(self, titre):
    #given a song title, find its corresponding url
      search_keyword= (remover(str(titre[0]) + " "+str(titre[1])+' audio')).lower()
      search_keyword = nostuff(search_keyword)
      print("Searching for " + search_keyword)
      search_keyword= search_keyword.replace(" ", "+")
      print(search_keyword)

      url = "https://www.youtube.com/results?search_query=" + search_keyword
      html = urllib.request.urlopen(url)

      video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

      if video_ids:
        self.urls.append("https://www.youtube.com/watch?v=" + video_ids[0])

      else:
        url1 = "https://www.youtube.com/results?search_query=" + "".join((remover(str(titre[0]) + " "+str(titre[1]))).lower().split())
        html1 = urllib.request.urlopen(url1)
        video_ids1 = re.findall(r"watch\?v=(\S{11})", html1.read().decode())

        if video_ids1:
          self.urls.append("https://www.youtube.com/watch?v=" + video_ids1[0])


  def gendownloads(self, dire):
  #loop over all urls in list and download each one of them
    for i in range (len(self.urls)):
      if self.urls[i]:
        self.download(self.urls[i], dire)


  def download(self, url, dire):
  #download mp3 given a youtube url
    print(url)
    video = YouTube(url).streams.filter(only_audio=True).first()
  
    # check for destination to save file
      
    # download the file
    out_file = video.download(output_path=dire)
      
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    print(out_file, new_file)
    self.conv(out_file, new_file, dire)
      
    # result of success
    print(YouTube(url).title + " has been successfully downloaded.")
    self.filenames.append(new_file)
  
  @staticmethod # no self parameters
  def conv(mp4, mp3, dire):
    # convert mp4 downloaded to an mp3
    audioclip = AudioFileClip(mp4)
    audioclip.write_audiofile(mp3)
    audioclip.close()
    # linux 
    cwd = os.getcwd()
    dir_name = os.path.join(cwd, dire)
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".mp4"):
            os.remove(os.path.join(dir_name, item)) # delete the mp4 

  
  def meta(self):
    # set metadate for all mp3s
    for i in range(len(self.titres)):
      audiofile = eyed3.load(self.filenames[i])
      audiofile.initTag()
      audiofile.tag.artist = self.titres[i][1]
      audiofile.tag.album = self.titres[i][2]
      audiofile.tag.title = self.titres[i][0]
      date = rem(self.titres[i][4]) # convert date to normal format
      audiofile.tag.release_date = date

      image = self.titres[i][3]

      lyrics = getlyrics(self.titres[i])
      if lyrics: #check if there are some lyrics
        audiofile.tag.lyrics.set(lyrics)

      response = opener.open(image)  
      imagedata = response.read() # get image from url

      type_="image/jpeg"
      audiofile.tag.images.set(3, imagedata, type_, description=u"album art")


      audiofile.tag.save(encoding='utf-8')

  def assemble(self, data, dire):
    self.getdata(data)
    self.findall()
    self.gendownloads(dire)
    self.meta()

file = str(input("Specify your csv file : "))
dire= str(input("Create a name for your music directory "))

with open(file, 'rb') as source_file: # convert to needed format 
  with open("16.csv", 'w+b') as dest_file:
    contents = source_file.read()
    dest_file.write(contents.decode('utf-8').encode('utf-16'))

Spotscrape().assemble("16.csv", dire)
