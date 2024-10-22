# FROM ubuntu:22.04 as base
FROM python:3.12 AS curl

RUN useradd -s /bin/bash -d /home/curl --uid=1000 -m curl

# Install npm
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get clean -y && \
    pip install poetry && \
    rm -rf /var/lib/apt/lists/*

# The user ubuntu is already created in the base image
USER curl
WORKDIR /home/curl

# Create a directory and copy the rest of curl into image
RUN mkdir -p /home/curl/aivm-bot
COPY --chown=curl:curl . aivm-bot

WORKDIR /home/curl/aivm-bot
RUN poetry install

# Execute aivm-devnet in background and poetry run aivm-bot
CMD ["sh", "-c", "poetry run aivm-devnet & poetry run aivm-bot"]
