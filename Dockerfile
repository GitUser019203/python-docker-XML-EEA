FROM python:latest

RUN apt-get update \
    && apt-get install -y \
    grep \
    net-tools \
    ncat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
