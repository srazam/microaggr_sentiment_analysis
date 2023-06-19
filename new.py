import csv
import time
from googleapiclient.discovery import build

# Set your API key and YouTube API service name
API_KEY = "AIzaSyDGH2Sddkb-KLDSWErXWEVCJzx4d42EfTU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Set the video ID and the number of comments to retrieve
VIDEO_ID = "wUn05hdkhjM"
MAX_RESULTS = 1000

# Create a CSV file and write header
csv_file = open("comments.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Video ID", "Comment", "Comment ID", "Published At", "Updated At", "Likes"])

# Create a YouTube API client
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

next_page_token = None
comment_count = 0

# Retrieve comments until the desired number is reached
while comment_count < MAX_RESULTS:
    # Calculate the number of results to retrieve for the current page
    remaining_comments = MAX_RESULTS - comment_count
    results_to_retrieve = min(100, remaining_comments)

    # Retrieve comments from the video for the current page
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        maxResults=results_to_retrieve,
        pageToken=next_page_token
    ).execute()

    # Iterate over the comments and write them to the CSV file
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]
        video_id = comment["videoId"]
        text = comment["textOriginal"]
        comment_id = item["id"]
        published_at = comment["publishedAt"]
        updated_at = comment["updatedAt"]
        likes = comment["likeCount"]

        csv_writer.writerow([video_id, text, comment_id, published_at, updated_at, likes])
        comment_count += 1

    # Check if there are more pages of comments
    next_page_token = response.get("nextPageToken")

    # Pause for 1 second before making the next API request
    time.sleep(1)

    if not next_page_token:
        break

# Close the CSV file
csv_file.close()

print("Comments extracted and saved to comments.csv")