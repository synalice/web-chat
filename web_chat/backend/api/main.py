from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from web_chat.backend.db.models import Post
from web_chat.backend.db.mongo import insert_into_mongodb, get_all_posts

app = FastAPI()

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.put("/web-chat/posts/new")
async def post_message(message: Post):
	await insert_into_mongodb(message, "messages_collection")
	return {"status": "OK"}


@app.put("/web-chat/posts/get_all")
async def get_all_messages():
	await get_all_posts()
	return {"status": "OK"}
