import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import time
import logging
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

app = FastAPI()

# Adding CORS as a middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

# MongoDB Client Setup using motor
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.test_SSE

class StreamData(BaseModel):
    name: str
    description: str
    price: float
    category: str
    created_at: str

# Streaming data from MongoDB every 10 seconds
async def event_stream():
    try:
        while True:
            # Fetch all data from the MongoDB collection
            items = await db.items.find().to_list(length=100)  # Asynchronous MongoDB query

            # Format data as JSON-like stream
            data = [{"name": item["name"], "description": item["description"], "price": item["price"],
                     "category": item["category"], "created_at": item["created_at"].strftime("%Y-%m-%d %H:%M:%S")}
                    for item in items]

            logging.debug(f"Sending data: {data}")

            yield f"data: {data}\n\n"
            await asyncio.sleep(10)  # Async sleep to avoid blocking the event loop
    except Exception as e:
        logging.error(f"Error in event_stream: {e}")
        raise HTTPException(status_code=500, detail="Stream Error")

# Streaming endpoint for the client to consume data
@app.get("/stream")
async def stream():
    try:
        return StreamingResponse(event_stream(), media_type="text/event-stream")
    except Exception as e:
        logging.error(f"Error in /stream: {e}")
        raise HTTPException(status_code=500, detail="Streaming Error")















































# import asyncio
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import StreamingResponse
# import time
# import logging
# from fastapi.middleware.cors import CORSMiddleware
# from motor.motor_asyncio import AsyncIOMotorClient
# from pydantic import BaseModel
# from pymongo import MongoClient
# from starlette.responses import JSONResponse
#
# app = FastAPI()
#
# # Adding CORS as a middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# # Enable detailed logging
# logging.basicConfig(level=logging.DEBUG)
#
# # # MongoDB Client Setup
# # client = AsyncIOMotorClient("mongodb://localhost:27017")  # Update with your MongoDB URI
# # db = client.test_SSE  # Ensure this database name matches your MongoDB setup
#
# # Define a Pydantic model for the streamed data
# # class StreamData(BaseModel):
# #     timestamp: str
# #     data: str
#
# # async def event_stream():
# #     try:
# #         while True:
# #             # Generate the current server time
# #             current_time = time.strftime("%Y-%m-%d %H:%M:%S")
# #             data = f"My current server time: {current_time}"
# #             logging.debug(f"Sending data: {data}")
# #
# #             # Store data in MongoDB
# #             stream_data = StreamData(timestamp=current_time, data=data)
# #             await store_data(stream_data)  # Store the data asynchronously
# #
# #             yield f"data: {data}\n\n"
# #             await asyncio.sleep(10)  # Use asyncio.sleep instead of time.sleep
# #     except Exception as e:
# #         logging.error(f"Error in event_stream: {e}")
# #         raise HTTPException(status_code=500, detail="Stream Error")
#
# # Storing data in db
# # async def store_data(stream_data: StreamData):
# #     try:
# #         logging.debug(f"Storing data in MongoDB: {stream_data.dict()}")
# #         await db.event_coll.insert_one(stream_data.dict())  # Ensure 'event_coll' is your collection name
# #     except Exception as e:
# #         logging.error(f"Error storing data in MongoDB: {e}")
# #         raise HTTPException(status_code=500, detail="Database Error")
#
# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["test_SSE"]
# collection = db["items"]
#
# @app.get("/stream_data")
# async def stream_data():
#     while True:
#         # Fetch all data from the MongoDB collection
#         data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
#         yield JSONResponse(content=data)  # Send data to the client
#         time.sleep(10)  # 10-second delay before sending the next batch of data
#
# # @app.get("/stream")
# # async def stream():
# #     try:
# #         return StreamingResponse(event_stream(), media_type="text/event-stream")
# #     except Exception as e:
# #         logging.error(f"Error in /stream: {e}")
# #         raise HTTPException(status_code=500, detail="Streaming Error")
