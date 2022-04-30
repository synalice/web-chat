from __future__ import annotations

from pydantic import BaseModel, Field


class Post(BaseModel):
	"""
	Default class for all things that are sent by user

	TODO: probably needs escaping to prevent any malicious input
	"""
	id: int = Field(..., alias='_id')
	date: str
	content: str | bytes
