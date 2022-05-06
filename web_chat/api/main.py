from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from web_chat.db.models import Post
from web_chat.db.mongo import insert_into_mongodb, get_all_posts_db, get_last_id_db

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

MONGO_COLLECTION = "messages_collection"
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/web-chat/", response_class=HTMLResponse)
async def render_html_page(request: Request, reversed_order: bool = False):
	if reversed_order:
		return TEMPLATES.TemplateResponse(
			"posts.html.jinja2",
			{"request": request, "posts": await get_all_posts_db(MONGO_COLLECTION, reversed_order=True)}
		)
	else:
		return TEMPLATES.TemplateResponse(
			"posts.html.jinja2",
			{"request": request, "posts": await get_all_posts_db(MONGO_COLLECTION)}
		)


@app.put("/web-chat/posts/new")
async def put_new_message(message: Post):
	await insert_into_mongodb(message, MONGO_COLLECTION)
	return {"status": "OK"}


@app.get("/web-chat/posts/get_all")
async def get_all_posts(reversed_order: bool = False):
	if reversed_order:
		return {"posts": await get_all_posts_db(MONGO_COLLECTION, reversed_order=True)}
	else:
		return {"posts": await get_all_posts_db(MONGO_COLLECTION)}


@app.get("/web-chat/posts/get_last_id")
async def get_last_id():
	return {"last_id": await get_last_id_db(MONGO_COLLECTION)}
