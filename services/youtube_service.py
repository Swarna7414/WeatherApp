import requests
from config.settings import YOUTUBE_API_KEY

def get_youtube_vids(location_name):
    """get youtube videos for a location"""
    try:
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'part': 'snippet',
            'q': f"{location_name} travel guide",
            'type': 'video',
            'maxResults': 5,
            'key': YOUTUBE_API_KEY
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return [{
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                'video_id': item['id']['videoId'],
                'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            } for item in data.get('items', [])]
        return []
    except Exception as e:
        print(f"youtube api error: {e}")
        return []
