import os
import time

from pymongo import MongoClient

from web_chat.backend.db.models import Post

MONGODB_URL = os.environ.get("MONGODB_URL")
DB_NAME = os.environ.get("DB_NAME")

client: MongoClient = MongoClient(f"{MONGODB_URL}")
db = client[f"{DB_NAME}"]


async def add_id_to_post(post: dict, collection: str):
	"""
	Adds and id to the received post

	:param collection:
	:param post:
	:return:
	"""
	post["_id"] = await get_last_id_db(collection) + 1
	return post


async def add_date_to_post(post: dict):
	"""
	Adds a date to the received post

	:param post:
	:return:
	"""
	post["date"] = time.time()
	return post


async def insert_into_mongodb(post: Post, collection: str) -> None:
	"""
	Inserts a Post model into the database

	:param collection:
	:param post:
	:return:
	"""
	post = post.dict(by_alias=True)
	post = await add_id_to_post(post, collection)
	post = await add_date_to_post(post)
	db[collection].insert_one(post)


async def get_one_last_post():
	"""
	TODO

	:return:
	"""
	...


async def get_all_posts_db(collection: str) -> list:
	"""
	Gets all documents from specified collection

	:return:
	"""
	return list(db[collection].find())


async def get_last_id_db(collection: str):
	"""
	Gets id of most recent document in the database

	:return:
	"""
	try:
		return (list(db[collection].find())[-1]).get("_id")
	except IndexError:
		return 0
