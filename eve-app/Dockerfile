FROM python:3.7.5-alpine3.9

WORKDIR /app

ADD requirements.txt /app

RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del build-dependencies

ADD . /app