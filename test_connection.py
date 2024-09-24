import os
from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient

MONGODB_URI = os.getenv('MONGODB_URI')
print(f"MONGODB_URI: {MONGODB_URI}")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set.")

try:
    client = MongoClient(MONGODB_URI)
    db = client.get_default_database()
    print("Connection successful!")
    # List collections
    print("Collections:", db.list_collection_names())
except Exception as e:
    print(f"Error: {e}")
