FROM ruby:3.3.0

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev vim

RUN mkdir /app
WORKDIR /app
