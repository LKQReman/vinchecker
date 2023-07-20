# Dockerfile
FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y && \
    python -m pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 