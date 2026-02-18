#import pymongo library = pymongo is a library/module to interact with mongosh with python
import pymongo

from pymongo import MongoClient
client = MongoClient()
db = client["starwars"]

##pymongo interaction commands are similar but not the same as mongosh
# mongosh = db.collection.insertOne() vs pymongo = db.collection.insert_one()
# mongosh = db.collection.updateMany() vs pymongo = db.collection.update_many()

#search using pymongo
#Luke skywalker info
luke = db.characters.find_one({"name": "Luke Skywalker"})
print(luke)


#Darth vader height
print(db.characters.find_one({"name": "Darth Vader"}, {"name":1,"height":1, "_id":0}))


# Find all characters with yellow eyes (names and eye color only)
for doc in db.characters.find({"eye_color": "yellow"}):
    print(doc["name"], doc["eye_color"])

# Find all male characters, limit to 3
for man in db.characters.find({"gender": "male"}).limit(3):
 print(man)

droids = db.characters.find({"species.name": "Droid"})
for droid in droids:
    print(droid["name"])

# Find the height of Darth Vader (only name and height outputted)
print(db.characters.find_one(
      {"name": "Darth Vader"},
      {"name": 1, "height": 1, "_id": 0})
      )

# Finding all humans whose homeworld is Alderaan
for human in db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"}):
    print(human["name"])
