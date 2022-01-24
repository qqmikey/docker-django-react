FROM python:3.10
RUN apt-get update
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
