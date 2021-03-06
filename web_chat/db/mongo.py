import os
import time

from pymongo import MongoClient

from web_chat.api.utils.utils import convert_timestamp_to_date
from web_chat.db.models import Post

MONGODB_URL = os.environ.get("MONGODB_URL")
DB_NAME = os.environ.get("DB_NAME")

client: MongoClient = MongoClient(f"{MONGODB_URL}")
db = client[f"{DB_NAME}"]


async def add_id_to_post(post: dict, collection: str):
	"""
	Adds and id to the received post

	:param post: Post model
	:param collection: Mongo collection
	:return:
	"""
	post["_id"] = await get_last_id_db(collection) + 1
	return post


async def add_date_to_post(post: dict):
	"""
	Adds a date to the received post

	:param post: Post model
	:return:
	"""
	post["date"] = time.time()
	return post


async def insert_into_mongodb(post: Post, collection: str) -> None:
	"""
	Inserts a Post model into the database

	:param post: Post model
	:param collection: Mongo collection
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
	raise NotImplementedError


async def get_all_posts_db(collection: str, reversed_order: bool = False, convert_timestamp: bool = True) -> list:
	"""
	Gets all documents from specified collection

	:param convert_timestamp: Determines if timestamp should be converted to human-readable date
	:param collection: Mongo collection
	:param reversed_order: Determines if the posts should be returned in reversed order
	:return:
	"""
	# TODO: This code like pure concentrated shit. Is there a better way I'm not seeing?
	if reversed_order is True:
		returned_value = list(db[collection].find())  # returned with IDs [1, 2, 3, 4, 5...]
	else:
		returned_value = list(db[collection].find())[::-1]  # returned with IDs [5, 4, 3, 2, 1...]

	if convert_timestamp is True:
		returned_value = await convert_timestamp_to_date(returned_value)

	return returned_value


async def get_last_id_db(collection: str):
	"""
	Gets id of most recent document in the database

	:param collection: Mongo collection
	:return:
	"""
	try:
		return (list(db[collection].find())[-1]).get("_id")
	except IndexError:
		return 0
