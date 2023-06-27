import csv
from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API Key
api_key = 'AIzaSyDGH2Sddkb-KLDSWErXWEVCJzx4d42EfTU'

# Replace 'VIDEO_ID' with the ID of the YouTube video you want to extract comments from
video_id = '6ZfuNTqbHE8'                                           

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Retrieve the first page of comments
response = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    maxResults=100,
    order='time'
).execute()

# Process the first page of comments
comments = []
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    comment_data = {
        'video_id': comment['videoId'],
        'comment_id': item['id'],
        'published_at': comment['publishedAt'],
        'updated_at': comment['updatedAt'],
        'likes': comment['likeCount'],
        'text': comment['textOriginal']
    }
    comments.append(comment_data)

# Check if there are more comments
while 'nextPageToken' in response:
    next_page_token = response['nextPageToken']
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        order='time',
        pageToken=next_page_token
    ).execute()

    # Process the next page of comments
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comment_data = {
            'video_id': comment['videoId'],
            'comment_id': item['id'],
            'published_at': comment['publishedAt'],
            'updated_at': comment['updatedAt'],
            'likes': comment['likeCount'],
            'text': comment['textOriginal']
        }
        comments.append(comment_data)

        # Exit the loop if we have reached the desired number of comments
        if len(comments) >= 200:
            break

    # Exit the loop if we have reached the desired number of comments
    if len(comments) >= 200:
        break

# Write the comments to a CSV file
filename = 'youtube_comments.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Video ID', 'Comment ID', 'Published At', 'Updated At', 'Likes', 'Comment Text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for comment in comments:
        writer.writerow({
            'Video ID': comment['video_id'],
            'Comment ID': comment['comment_id'],
            'Published At': comment['published_at'],
            'Updated At': comment['updated_at'],
            'Likes': comment['likes'],
            'Comment Text': comment['text']
        })