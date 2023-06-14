FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

WORKDIR /eventsphere

COPY Pipfile Pipfile.lock /eventsphere/
RUN pip install pipenv && pipenv install --system

COPY . /eventsphere/