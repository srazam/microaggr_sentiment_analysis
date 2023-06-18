import csv
from googleapiclient.discovery import build

api_key = "AIzaSyDGH2Sddkb-KLDSWErXWEVCJzx4d42EfTU"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_comments(video_id, max_results):
    comments = []
    next_page_token = None

    while True:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=min(max_results, 100),
            pageToken=next_page_token
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            author = comment['authorDisplayName']
            text = comment['textDisplay']
            published_at = comment['publishedAt']

            comments.append({
                'author': author,
                'text': text,
                'published_at': published_at,
                'video_id': video_id
            })

        next_page_token = response.get('nextPageToken')

        if not next_page_token or len(comments) >= max_results:
            break

    return comments

def save_comments_to_csv(comments, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['author', 'text', 'published_at', 'video_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(comments)

# Video ID of the YouTube video
video_id = "wUn05hdkhjM"

# Maximum number of comments to retrieve
max_results = 18

# Retrieve comments
comments = get_video_comments(video_id, max_results)

# Save comments to a CSV file
save_comments_to_csv(comments, 'comments.csv')
