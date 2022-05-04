from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from web_chat.backend.db.models import Post
from web_chat.backend.db.mongo import insert_into_mongodb, get_all_posts_db, get_last_id_db

app = FastAPI()
mongo_collection = "messages_collection"

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.put("/web-chat/posts/new")
async def put_new_message(message: Post):
	await insert_into_mongodb(message, mongo_collection)
	return {"status": "OK"}


@app.get("/web-chat/posts/get_all")
async def get_all_posts():
	return {"posts": await get_all_posts_db(mongo_collection)}


@app.get("/web-chat/posts/get_last_id")
async def get_last_id():
	return {"last_id": await get_last_id_db(mongo_collection)}
