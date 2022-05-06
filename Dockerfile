FROM python:3.10

WORKDIR web-chat/
COPY pyproject.toml ./
RUN pip install pipx
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN	poetry install --no-root --no-dev

COPY web_chat/ /web-chat/web_chat/

ENV PYTHONPATH=$PYTHONPATH:/web-chat
WORKDIR /web-chat/web_chat/api/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

### This line is for debugging purposes. Uncomment if you need the container to run forever so that you can exec into it.
### ONLY use this for debugging purposes.
#ENTRYPOINT ["tail", "-f", "/dev/null"]
