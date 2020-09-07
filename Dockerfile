FROM python:3

WORKDIR /usr/src/app

COPY ./src/ ./
COPY ./config/ ./config