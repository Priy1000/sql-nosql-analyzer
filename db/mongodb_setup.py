from pymongo import MongoClient
import pandas as pd

def load_to_mongodb():
    data = pd.read_csv("books.csv")

    client = MongoClient("mongodb://localhost:27017/")
    db = client["books_db"]
    collection = db["books"]

    collection.delete_many({})
    collection.insert_many(data.to_dict("records"))
    print(" MongoDB Loaded")

if __name__ == "__main__":
    load_to_mongodb()
