# start from base
FROM ubuntu:18.04

LABEL maintainer="izaazira <izza.gwcc@gmail.com>"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev build-essential python3-flask

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "./api/app.py" ]
