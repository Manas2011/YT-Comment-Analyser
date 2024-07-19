import googleapiclient.discovery
import pandas as pd

# Set up the YouTube API client
api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyCuaHidtnZZ5vMsO7J6mh5dqk09puziHAI"  # Replace with your API key

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

def get_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    response = request.execute()

    while request:
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        if "nextPageToken" in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                textFormat="plainText",
                pageToken=response["nextPageToken"]
            )
            response = request.execute()
        else:
            break

    return comments

video_id = "UmnCZ7-9yDY"  # Replace with the YouTube video ID
comments = get_comments(video_id)
df = pd.DataFrame(comments, columns=["comment"])
df.to_csv("comments.csv", index=False)
