from __future__ import annotations

from pydantic import BaseModel


class Post(BaseModel):
	"""
	Default class for all things that are sent by user

	TODO: probably needs escaping to prevent any malicious input
	"""
	content: str | bytes
