# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

from googleapiclient.discovery import build

DEVELOPER_KEY = "AIzaSyDGH2Sddkb-KLDSWErXWEVCJzx4d42EfTU"

youtube = build(
    "youtube", "v3", developerKey = DEVELOPER_KEY)

def comment_threads(channelID, to_csv = False):
    request = youtube.commentThreads().list(
        part="id.replies, snippet",
        videoId = channelID,
        maxResults = 5
    )
    response = request.execute()
    print(response)

def main():
    comment_threads('UCykOzZdQ5wLKvaAcD1Um5xQ')
    

if __name__ == "__main__":
    main()