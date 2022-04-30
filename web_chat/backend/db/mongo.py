import os

from pymongo import MongoClient

MONGODB_URL = os.environ.get("MONGODB_URL")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(f"{MONGODB_URL}")
db = client[f"{DB_NAME}"]
collection = db['messages_collection']


async def insert_into_mongodb(model) -> None:
	post = model.dict(by_alias=True)
	collection.insert_one(post)


async def get_one_last_post():
	...


async def get_all_posts():
	...
