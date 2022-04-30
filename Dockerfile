FROM python:3.10

COPY poetry.lock pyproject.toml README.md web-chat/
RUN mkdir web-chat/web_chat/ && touch web-chat/web_chat/__init__.py
WORKDIR web-chat/
RUN	pip install --no-cache-dir .

COPY web_chat/ web_chat/

ENV PYTHONPATH=$PYTHONPATH:/web-chat/

WORKDIR web_chat/backend/api/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

## This line is for debugging purposes. Uncomment if you need the container to run forever so that you can exec into it.
## ONLY use this for debugging purposes.
#ENTRYPOINT ["tail", "-f", "/dev/null"]
