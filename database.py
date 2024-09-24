import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
print(f"MONGODB_URI in database.py: {MONGODB_URI}")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set. Please check your .env file.")

try:
    client = MongoClient(MONGODB_URI)
    db = client.get_default_database()
    collection = db['videos']
    print("Connected to MongoDB Atlas successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    raise

def store_videos(videos):
    if videos:
        # Remove duplicates before inserting
        existing_titles = set(item['title'] for item in collection.find({}, {'title': 1}))
        new_videos = [video for video in videos if video['title'] not in existing_titles]

        if new_videos:
            collection.insert_many(new_videos)
            print(f"Inserted {len(new_videos)} new videos into the database.")
        else:
            print("No new videos to insert.")
    else:
        print("No videos to store.")