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
    db = client.get_default_database()
    collection = db['videos']
    print("Connected to MongoDB Atlas successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    raise

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
    else:
        query = None

    if query:
        videos = list(collection.find({"title": {"$regex": query, "$options": "i"}}))
    else:
        videos = list(collection.find())

    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
