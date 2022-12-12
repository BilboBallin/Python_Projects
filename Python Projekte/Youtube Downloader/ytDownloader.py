from pytube import YouTube
from sys import argv
import os
from moviepy.editor import *

#which youtube mp4 (-> mp3) you want to download?
link = input("Welches YT-Lied möchtest du herunterladen? ")
#link = argv[1]
yt = YouTube(link)

#print('Title: ', yt.title)
#print('Views: ', yt.views)

yd = yt.streams.get_highest_resolution() #get highest resolution lol

#save (safe) and sound
yd.download("/home/proman/Desktop/Python Projekte/Youtube Downloader/ytdownloads") #note: change direction for own path

#convert mp4 to mp3
video = VideoFileClip(os.path.join("/home/proman/Desktop/Python Projekte/Youtube Downloader/ytdownloads/", f"{yt.title}.mp4")) #note: change direction for own path
video.audio.write_audiofile(os.path.join("/home/proman/Desktop/Python Projekte/Youtube Downloader/ytdownloads/", f"{yt.title}.mp3")) #note: change direction for own path

# to delete the .mp4 video file:
mp4_path = f"/home/proman/Desktop/Python Projekte/Youtube Downloader/ytdownloads/{yt.title}.mp4" #note: change direction for own path
os.remove(mp4_path)