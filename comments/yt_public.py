# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from dotenv import load_dotenv

from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv("API_KEY")

youtube = build(
    "youtube", "v3", developerKey = API_KEY)

def comment_threads(channelID, to_csv = False):
    request = youtube.commentThreads().list(
        part="id.replies, snippet",
        videoId = channelID, 
        maxResults = 1000
    )
    response = request.execute()
    print(response)

def main():
    comment_threads('m9EX0f6V11Y')
    

if __name__ == "__main__":
    main()