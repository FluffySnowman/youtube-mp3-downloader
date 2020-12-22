import youtube_dl

video_url = input("Link to download: ")
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