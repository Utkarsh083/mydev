from pytube import YouTube

url='https://www.youtube.com/watch?v=aiEuzkJDwUg'
my_video=YouTube(url)

print(my_video.title)
my_video=my_video.streams.get_highest_resolution()

my_video.download()