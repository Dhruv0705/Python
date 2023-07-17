from pytube import YouTube
from sys import argv

# Total amounts of video links
links = int(input("Enter the number of Youtube video Links to download: "))

# Stores all links within list
linksList = []

# Ask user for links one per line:
print("\nEnter all the links one per line:")

for i in range(0, links):

    # input each link per line
    linksEntered = input()
    
    # Appends all links entered within list
    linksList.append(linksEntered)

# Showing all details for videos and downloading them one by one
for i in range(0, links):
    link = linksList[i]
    yt = YouTube(link)

    print("\nDetails for Video", i+1, "\n")
    print("Title of video:   ", yt.title)
    print("Number of views:  ", yt.views)
    print("Length of video:  ", yt.length, "seconds")
    
    # Filter to select only progressive streams
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamList = stream.split(", ")
    print("\nAll available options for downloads:\n")
    
    # Loop around all available streams and print them for user to decide
    for i in range(0, len(streamList)):
        st = streamList[i].split(" ")
        print(i+1, ") ", st[1], " and ", st[3], sep='')
    
    # Ask user the tag for the stream to download
    tag = int(input("\nEnter the itag of your preferred stream to download:   "))
    ys = yt.streams.get_by_itag(tag)
    
    print("\nDownloading...")
    ys.download('DownloadedVideos')
    print("\nDownload completed!!")
    print()










'''
# Title of video
print("Title: ", uTube.title)

# Number of views of video
print("Number of views: ", uTube.views)

# Length of the video
print("Length of video: ", uTube.length, "seconds")

# Description of video
print("Description: ", uTube.description)

# Rating of video
print("Ratings: ", uTube.rating)

# Grabs highest possible quality of video
uTube = uTube.streams.get_highest_resolution()

# Starting Download
print("Downloading...")
uTube.download('DownloadedVideos')

print("Download Complete!")
'''
