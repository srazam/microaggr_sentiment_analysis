#For getting comments from a specific YouTube channel

from googleapiclient.discovery import build
#"pretty print"; gives it the nice format once program is ran 
from pprint import pprint

CHANNEL_ID = "UCLj_i7yL-8FZrdQA6eE4iqQ"

# Creating an object of the instance of the API
def get_youtube():
    DEVELOPER_KEY = 'AIzaSyDGH2Sddkb-KLDSWErXWEVCJzx4d42EfTU'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    return youtube

#Searching all the videos for a particular channel ID
youtube = get_youtube()
request = youtube.search().list(
    part="snippet",
    type = "video",
    channelId="UCLj_i7yL-8FZrdQA6eE4iqQ",
    maxResults = 50
)
response = request.execute()
video_ids = []
for item in response['items'][:1]:
    title = item['snippet']['title']
    videoId = item['id']['videoId']
    video_ids.append(videoId)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        maxResults = 50
    )
    response = request.execute()
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        comment_text = comment["snippet"]["textDisplay"]

        print(author + " - " + comment_text)