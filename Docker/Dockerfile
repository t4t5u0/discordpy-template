FROM python:3.10-slim as builder

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./


# RUN poetry export -f requirements.txt > requirements.txt

RUN apt-get update && apt-get install -y git
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev --no-interaction

FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# COPY --from=builder /usr/src/app/requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .
COPY --from=builder /app/.venv /app/.venv
COPY src /app/src
