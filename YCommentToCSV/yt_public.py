# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from dotenv import load_dotenv

from  googleapiclient.discovery import build
API_KEY = os.getenv('API_KEY')
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "API_KEY"

    youtube =build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="id,snippet,replies",
        order="relevance",
        videoId="MWxWVCiRbsQ"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()