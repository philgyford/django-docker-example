FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Uncomment this when https://github.com/pypa/pipenv/issues/2924 is resolved:
#RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile /app/
RUN pipenv install --skip-lock --system --dev

COPY . /app/
