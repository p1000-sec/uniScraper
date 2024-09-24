import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def fetch_youtube_videos(query):
    try:
        url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'part': 'snippet',
            'q': query,
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 10
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        videos = []
        for item in data.get('items', []):
            snippet = item['snippet']
            video = {
                'title': snippet['title'],
                'description': snippet['description'],
                'thumbnail_url': snippet['thumbnails']['high']['url'],
                'channel': snippet['channelTitle'],
                'published_at': snippet['publishedAt'],
                'platform': 'YouTube'
            }
            videos.append(video)
        return videos
    except Exception as e:
        print(f"Error fetching YouTube videos: {e}")
        return []

def fetch_dailymotion_videos(query):
    try:
        url = 'https://api.dailymotion.com/videos'
        params = {
            'search': query,
            'fields': 'title,description,thumbnail_url,channel.name,created_time',
            'limit': 10
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        videos = []
        for item in data.get('list', []):
            video = {
                'title': item.get('title'),
                'description': item.get('description'),
                'thumbnail_url': item.get('thumbnail_url'),
                'channel': item.get('channel.name'),
                'published_at': datetime.utcfromtimestamp(item.get('created_time')).isoformat() if item.get('created_time') else None,
                'platform': 'Dailymotion'
            }
            videos.append(video)
        return videos
    except Exception as e:
        print(f"Error fetching Dailymotion videos: {e}")
        return []

if __name__ == '__main__':
    videos = fetch_youtube_videos('test query')
    print(videos)