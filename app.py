import asyncio
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.trip_planner
collection = db["trip_data"]

# Function to fetch trip data from MongoDB
async def fetch_trip_data():
    trip_data = await collection.find_one({"title": "Shimla Trip Guide"})
    if trip_data and "steps" in trip_data:
        return trip_data["steps"]
    return []

async def event_stream():
    trip_content = await fetch_trip_data()
    if trip_content:
            # while True:
                for step in trip_content:
                    step_json = json.dumps(step)
                    yield f"data: {step_json}\n\n"
                    await asyncio.sleep(2)
    else:
        yield "data: No content found\n\n"


@app.get("/stream_trip")
async def stream_trip():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
