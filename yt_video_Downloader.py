from pytube import YouTube

try:
    link = "https://www.youtube.com/watch?v=QmcJVZkdiTk" #here paste the yt video link you want to download
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download("C:/Users/rohan/Downloads") # here paste the adress of your folder where you want to get the video
    print("Download complete")
except Exception as e:

    print("Error:",e)

# it can give you error sometime if your internet blockchain reject the request
