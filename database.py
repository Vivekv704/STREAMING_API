# database.py
import motor.motor_asyncio
from pymongo import MongoClient

# Replace 'your_mongodb_uri' with your actual MongoDB URI
MONGODB_URL = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client['SSE_TEST']  # Replace with your database name
collection = database['EVENTS']  # Replace with your collection name
