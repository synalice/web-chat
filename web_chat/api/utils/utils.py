from datetime import datetime


async def convert_timestamp_to_date(posts: list) -> dict:
	for post in posts:
		post["date"] = str(datetime.fromtimestamp(post["date"]))
	return posts
