from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from web_chat.backend.api.models import Post

app = FastAPI()

origins = [
	"http://localhost",
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/")
async def home(request: Request):
	return {"Hello": "World"}


@app.post("/web-chat/posts/new")
async def update_item(message: Post):
	with open("../database.txt", "a") as f:
		if not message.content:
			pass
		else:
			f.write(message.content + "\n")
	return {"status": "OK"}
