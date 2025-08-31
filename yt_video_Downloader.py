from pytube import YouTube

try:
    link = "https://www.youtube.com/watch?v=QmcJVZkdiTk"
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download("C:/Users/rohan/Downloads")
    print("Download complete ✅")
except Exception as e:
    print("Error:",e)