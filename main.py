from pytube import YouTube

link = input("Enter the Video link: ")
video = YouTube(link)

print("\n")
print("Title: " + video.title)
print("\n")
print("Thumbnail Image: " + video.thumbnail_url)
print("\n")
stream = video.streams.get_by_itag(22)
stream.download()
print("success!")