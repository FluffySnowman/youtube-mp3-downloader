import tkinter
from tkinter import *


window = Tk()
window.geometry("250x120")

#Adding widgets

label1 = Label(window, text = "Link: ")
label1.pack( side = LEFT)

entrybox1 = Entry(window, bd = 5)
entrybox1.pack(side = RIGHT)

def doLink():
    link = entrybox1.get()
    print("Link to download: " + link)
    video_url = link
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])




button1 = Button(window, text = "Download", command = doLink)
button1.place(x = 150,y = 70)

window.mainloop()