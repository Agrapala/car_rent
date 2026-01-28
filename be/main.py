from fastapi import FastAPI
from pymongo import MongoClient
import time

app = FastAPI()

def get_db():
    for i in range(10):  # retry up to 10 times
        try:
            client = MongoClient("mongodb://mongo:27017", serverSelectionTimeoutMS=2000)
            client.server_info()  # force connection
            return client.carrental
        except Exception:
            print("Waiting for MongoDB...")
            time.sleep(3)
    raise Exception("MongoDB not reachable")

db = get_db()

@app.on_event("startup")
def seed_data():
    if db.cars.count_documents({}) == 0:
        db.cars.insert_many([
            {"name": "Toyota Corolla", "available": True},
            {"name": "Honda Civic", "available": True},
            {"name": "BMW X5", "available": False}
        ])

@app.get("/cars")
def get_cars():
    return list(db.cars.find({}, {"_id": 0}))

@app.get("/health")
def health():
    return {"status": "ok"}
