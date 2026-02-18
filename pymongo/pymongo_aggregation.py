import pymongo

from pymongo import MongoClient
client = MongoClient()
db = client["starwars"]

# What is the average height of all female characters in the collection?
avg_female_height = db.characters.aggregate([
    {"$match": {"gender": "female"}},
    {"$group": {"_id": "$gender", "avg_height": {"$avg": "$height"}}}
])

print(avg_female_height.next())
# Which characters is the tallest in the collection?
max_height = db.characters.aggregate([
    {"$group": {"_id": None, "max_height": {"$max": "$height"}}}
]).next()["max_height"]

for tallest in db.characters.find({"height": max_height}):
    print(tallest["name"], tallest["height"])

