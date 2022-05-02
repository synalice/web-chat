import os

from pymongo import MongoClient

from web_chat.backend.db.models import Post

MONGODB_URL = os.environ.get("MONGODB_URL")
DB_NAME = os.environ.get("DB_NAME")

client: MongoClient = MongoClient(f"{MONGODB_URL}")
db = client[f"{DB_NAME}"]


# collection = db['messages_collection']


async def insert_into_mongodb(post: Post, collection: str) -> None:
	"""
	Inserts a Post model into the database

	:param collection:
	:param post:
	:return:
	"""
	post = post.dict(by_alias=True)
	db[collection].insert_one(post)


async def get_one_last_post():
	"""
	TODO

	:return:
	"""
	...


async def get_all_posts_db(collection: str):
	"""
	Gets all documents from specified collection

	:return:
	"""
	return {"posts": list(db[collection].find())}


async def get_last_id_db(collection: str):
	"""
	Gets id of most recent document in the database

	:return:
	"""
	return {"last_id": (list(db[collection].find())[-1]).get("_id")}
