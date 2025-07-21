# youtube_client.py
from googleapiclient.discovery import build
import config

def search_for_video(query):
    """
    Searches YouTube for a video based on a query.
    Returns the URL of the top search result.
    """
    try:
        # Build the service object
        youtube = build('youtube', 'v3', developerKey=config.YOUTUBE_API_KEY)
        
        # Create the API request - FIXED: Use the youtube service object
        request = youtube.search().list(
            q=query,
            part='snippet',
            maxResults=1,  # We only want the top result
            type='video'
        )
        
        # Execute the request
        response = request.execute()
        
        # Get the video ID from the response
        if response['items']:
            video_id = response['items'][0]['id']['videoId']
            return f'https://www.youtube.com/watch?v={video_id}'
            
    except Exception as e:
        print(f"An error occurred with the YouTube API: {e}")
        return None

    return None