FROM python:3.11.2-alpine3.17
LABEL maintainer="apoorvabhishek.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /temporary/requirements.txt
COPY ./app /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk upgrade && \
    apk update && \
    apk add chromium && \
    apk add chromium-chromedriver && \
    /py/bin/pip install -r /temporary/requirements.txt && \
    rm -rf /temporary && \
    adduser \
        --disabled-password \
        --no-create-home \
        selenium-user

ENV PATH="/py/bin:$PATH"

USER selenium-user
