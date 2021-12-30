from pytube import YouTube

#pip install pytube

# USER HAVE TO ENTER THE URL VIDEO LINK TO DOWNLOAD IT
link=input("Enter the video URL link:")
try:
    # HERE OBJECT CREATION IS DONE
    yt=YouTube(link)
except:
    # TO HANDLE THE EXCEPTION
    print("OOPS!!! There is some issue with connection.")

# FILTER IS USED TO SELECT THE "MP4" EXTENSION 
mp4Files= yt.filter('mp4')

# HERE TO SET THE NAME OF THE FILE
yt.set_filename("Youtube Videos")

# SO HERE GET THE VIDEO WITH THE EXTENSION AND 
# THE RESOLUTION OF THE VIDEO THAT IS PASSED IN THE GET() FUNCTION
d_video= yt.get(mp4Files[-1].extension, mp4Files[-1].resolution)

try:
    # DOWNLOADING THE VIDEO
    d_video.download()
except:
    print("Ohh No!!! Some error...")

print("Congratulations!!! Video Downloaded")
