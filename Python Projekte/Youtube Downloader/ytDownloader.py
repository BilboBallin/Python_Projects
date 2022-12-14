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

yd = yt.streams.get_highest_resolution()

#save (safe) and sound
saved_video = yd.download() #note: output saved to the current working directory

#convert mp4 to mp3
video = VideoFileClip(saved_video) 
video.audio.write_audiofile(saved_video.replace(".mp4", ".mp3")) 

# to delete the .mp4 video file:
answer = input("Möchtest du das Video noch löschen? [y/n] ")
yes = {'yes', 'y', 'ye', ''}
no = {'no', 'n', 'noo'}
# you rly want to delete the video?
if answer in yes:
    os.remove(saved_video)
elif answer in no:
    pass
else:
    sys.stdout.write("Bitte antworte mit 'yes' or 'no'")
