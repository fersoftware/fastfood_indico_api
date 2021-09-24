# pull official base image
FROM python:3.8.12-alpine

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add build-base postgresql-dev gcc python3-dev musl-dev py3-numpy py3-pandas

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . .
