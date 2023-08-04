FROM python:3.11.4-slim-bullseye

# set work directory
WORKDIR /usr/src/ecourse

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .