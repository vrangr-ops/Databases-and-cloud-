import requests
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.openlibrary

# Open Library search API (JSON)
url = "https://openlibrary.org/search.json?q=lord+of+the+rings"

response = requests.get(url)
data = response.json()

# Extract book documents
docs = data.get("docs", [])

clean_books = []

for b in docs:
    clean_books.append({
        "title": b.get("title"),
        "authors": b.get("author_name", []),
        "author_keys": b.get("author_key", []),
        "first_publish_year": b.get("first_publish_year")
    })

if clean_books:

    db.books.insert_many(clean_books)
    print("Inserted:", db.books.count_documents({}))
else:
    print("No books found")

for index in clean_books.list_search_indexes():
    print(index)

client = MongoClient()
db = client["lotr"]
clean_books_collection = db["clean_books"]
clean_books = list(clean_books.find())

   