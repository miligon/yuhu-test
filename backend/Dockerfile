# Final Image
FROM python:3.12.0-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
RUN mkdir /backend/stati

COPY ./backend/requirements.txt /backend
RUN apt update
RUN apt install -y libpq-dev gcc 
RUN pip install --no-cache-dir -r /backend/requirements.txt
WORKDIR /backend