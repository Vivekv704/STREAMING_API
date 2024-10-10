from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["trip_planner"]
collection = db["trips"]

# Define the JSON data
trip_guide = {
  "title": "Shimla Trip Guide",
  "steps": [
    {
      "step": 1,
      "title": "Pick Your Travel Dates",
      "details": "Best Time to Visit: March to June (pleasant weather), December to February (snowfall). Plan your dates around long weekends if possible."
    },
    {
      "step": 2,
      "title": "Choose Your Mode of Transport",
      "details": "By Road: The drive from Chandigarh to Shimla takes around 3-4 hours by car. You can hire a private car or take a bus. Bus: Regular buses run from Chandigarh to Shimla. Taxi/Car Rental: You can rent a self-drive car or book a cab. By Train: You can take the Kalka-Shimla toy train, a UNESCO World Heritage site, for scenic views. By Air: The nearest airport is Jubbarhatti (around 23 km from Shimla), but flights are limited."
    },
    {
      "step": 3,
      "title": "Book Accommodation",
      "details": "Choose from various options depending on your budget: Luxury Hotels: Oberoi Cecil, Wildflower Hall Mid-range Hotels: Hotel Willow Banks, Hotel Combermere Budget Hotels: Hotel Shingar, Hotel White."
    },
    {
      "step": 4,
      "title": "Create a Basic Itinerary",
      "details": [
        {
          "day": 1,
          "description": "Arrival and Sightseeing: Reach Shimla by noon. Visit Mall Road, Christ Church, and The Ridge for shopping and leisure. Enjoy an evening stroll on Mall Road."
        },
        {
          "day": 2,
          "description": "Explore Kufri and Nearby Areas: Head to Kufri for adventure activities like horse riding, skiing (in winter), and tobogganing. Visit Green Valley and Himalayan Nature Park. In the evening, visit Jakhoo Temple or explore Lakkar Bazaar for wooden souvenirs."
        },
        {
          "day": 3,
          "description": "Mashobra/Naldehra & Departure: Visit Mashobra for a peaceful environment or head to Naldehra for a golf experience. Return to Shimla, have lunch, and depart for Chandigarh."
        }
      ]
    },
    {
      "step": 5,
      "title": "Budget Breakdown",
      "details": {
        "transport": "Bus: ₹500-₹1,000 per person, Taxi: ₹3,000-₹4,000 one way",
        "hotel_stay": "Budget: ₹2,000-₹4,000 per night, Mid-range: ₹5,000-₹10,000 per night",
        "food_and_activities": "Budget: ₹1,500-₹2,500 per person per day",
        "total_cost": "₹8,000 - ₹20,000 per person (depends on accommodation and activities)"
      }
    },
    {
      "step": 6,
      "title": "Pack Essentials",
      "details": "Warm clothes, Comfortable shoes, Personal ID, Power bank, camera, water bottle."
    },
    {
      "step": 7,
      "title": "Additional Tips",
      "details": "Book in advance, try local Himachali dishes, be mindful of the weather."
    }
  ]
}

# Insert the data into MongoDB
collection.insert_one(trip_guide)

print("Trip guide inserted successfully!")
