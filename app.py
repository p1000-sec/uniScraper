import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request
from pymongo import MongoClient

MONGODB_URI = os.getenv('MONGODB_URI')
print(f"MONGODB_URI in app.py: {MONGODB_URI}")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set. Please check your .env file.")

try:
    client = MongoClient(MONGODB_URI)
    db = client['video_database']
    collection = db['videos']
    print("Connected to MongoDB Atlas successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    raise

app = Flask(__name__)
videos = [
    {
        "title": "Sample Video",
        "platform": "YouTube",
        "thumbnail_url": "https://example.com/thumbnail.jpg",
        "channel": "Sample Channel",
        "published_at": "2023-01-01",
        "description": "This is a sample video description."
    }
]

@app.route('/')
def home():
    return render_template('video_app.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
