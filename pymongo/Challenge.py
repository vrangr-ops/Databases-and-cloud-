#import the neccssary libraries
import pymongo #connect to MongoDB
import requests #calls the SWAPI API.
import json #formatting JSON
from pymongo import MongoClient


# API for starships
url = "https://swapi.dev/api/starships/"
def extract_id(url):
    return int(url.rstrip("/").split("/")[-1])


response = requests.get(url)

# Convert the JSON response to Python dictionary

client = MongoClient("mongodb://localhost:27017/")
db = client.starwars
all_starships = []

while url:
    data = response.json()
    response = requests.get(url)
    all_starships.extend(data["results"])
    url = data["next"]



db.starships.insert_many(all_starships)
print("Starships data inserted into MongoDB local database")
print(db.starships.count_documents({}))

#Create "startships" collection in mongodb and populate with starship data (using object ids)
for ship in all_starships:
    pilot_urls = ship.get("pilots", [])
    pilot_ids = [extract_id(u) for u in pilot_urls]
    ship["pilot_ids"] = pilot_ids
    del ship["pilots"] 




