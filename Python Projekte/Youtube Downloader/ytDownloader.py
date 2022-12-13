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
saved_video = yd.download() #note: output saved to the current working directory

#convert mp4 to mp3
video = VideoFileClip(saved_video) 
video.audio.write_audiofile(saved_video.replace(".mp4", ".mp3")) 

# to delete the .mp4 video file:
os.remove(saved_video)