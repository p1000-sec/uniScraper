from scraper import fetch_youtube_videos, fetch_dailymotion_videos
from database import store_videos

def main():
    query = input("Enter a search query: ")
    youtube_videos = fetch_youtube_videos(query)
    dailymotion_videos = fetch_dailymotion_videos(query)
    all_videos = youtube_videos + dailymotion_videos
    store_videos(all_videos)

if __name__ == '__main__':
    main()