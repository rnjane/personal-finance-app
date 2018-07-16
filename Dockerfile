FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /finance-app

WORKDIR /finance-app

ADD . /finance-app/

RUN pip install -r requirements.txt