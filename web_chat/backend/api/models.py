from pydantic import BaseModel


class Post(BaseModel):
	id: int
	date: str
	content: str | bytes
