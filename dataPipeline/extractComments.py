'''
    Insert YouTube API Key and Video ID to extract the first 200 comments of a YouTube video. CSV files will be stored in 'rawData' folder.
'''

import csv
from googleapiclient.discovery import build
from pathlib import Path

api_key = 'YOUR_API_KEY'
video_ids = ['LIST OF VIDEO IDs HERE']                                      
file_names = ['FILENAMEHERE.csv', 'SECONDFILENAMEHERE.csv', ...] 

# YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

comments = []

for video_id, file_name in zip(video_ids, file_names):

    # First page of comments
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        order='time'
    ).execute()

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

    # Get up to 200 comments
    while 'nextPageToken' in response and len(comments) < 200:
        next_page_token = response['nextPageToken']
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            order='time',
            pageToken=next_page_token
        ).execute()

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

    # Convert comments to a csv file
    with open(Path('..') / 'rawData' / file_name, 'w', newline='', encoding='utf-8') as csvfile:
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