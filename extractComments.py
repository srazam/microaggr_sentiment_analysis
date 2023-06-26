import csv
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set your YouTube API key
API_KEY = 'AIzaSyDGH2Sddkb-KLDSWErXWEVCJzx4d42EfTU'

# Set the video ID for which you want to extract comments
VIDEO_ID = '6ZfuNTqbHE8'

# Set the maximum number of comments to retrieve
MAX_RESULTS = 1000

# Set the desired column names for the CSV file
FIELD_NAMES = ['video_id', 'comment_text', 'likes', 'published_at', 'updated_at', 'comment_id']

def retrieve_comments(api_key, video_id, max_results):
    try:
        # Build the YouTube API service
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Call the API to retrieve the video comments
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_results
        ).execute()

        # Process the comments and return the relevant information
        comments = []
        while response:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comment_info = {
                    'video_id': video_id,
                    'comment_text': comment['textDisplay'],
                    'likes': comment['likeCount'],
                    'published_at': comment['publishedAt'],
                    'updated_at': comment['updatedAt'],
                    'comment_id': item['snippet']['topLevelComment']['id']
                }
                comments.append(comment_info)

            #Check if there are more comments to retrieve
            if 'nextPageToken' in response:
                next_page_token = response['nextPageToken']
                response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    maxResults=max_results, 
                    pageToken=next_page_token
                ).execute()
            else:
                break

        return comments

    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')

def write_to_csv(comments):
    file_exists = os.path.isfile('youtube_comments.csv')

    with open('youtube_comments.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerows(comments)

# Retrieve and store the comments
comments = retrieve_comments(API_KEY, VIDEO_ID, MAX_RESULTS)
write_to_csv(comments)
