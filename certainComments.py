import csv
import googleapiclient.discovery
import googleapiclient.errors

def get_video_comments(api_key, video_id, max_results):
    # Create the YouTube API client
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    try:
        # Retrieve the comments using the YouTube API
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_results,
            order='time'  # Retrieve comments in chronological order
        ).execute()

        # Extract the relevant information from the API response
        comments = []
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'video_id': video_id,
                'author': comment['authorDisplayName'],
                'text': comment['textDisplay'],
                'published_at': comment['publishedAt'],
                'comment_id': item['id'],
                'parent_id': item['snippet']['parentId']
            })

        return comments

    except googleapiclient.errors.HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')

def save_comments_to_csv(comments, filename):
    # Define the CSV fieldnames
    fieldnames = ['video_id', 'author', 'text', 'published_at', 'comment_id', 'parent_id']

    # Write the comments to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(comments)

# Set your API key, video ID, and maximum number of comments to retrieve
api_key = 'AIzaSyDGH2Sddkb-KLDSWErXWEVCJzx4d42EfTU'
video_id = 'wUn05hdkhjM'
max_results = 18

# Retrieve the comments
comments = get_video_comments(api_key, video_id, max_results)

# Save the comments to a CSV file
save_comments_to_csv(comments, 'comments.csv')