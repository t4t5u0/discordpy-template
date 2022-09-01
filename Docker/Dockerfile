ARG PYTHON_ENV=python:3.10-slim 

FROM $PYTHON_ENV as builder

RUN apt-get update && apt-get install -y git
RUN pip install --upgrade pip && pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev --no-interaction


FROM $PYTHON_ENV as prod


COPY --from=builder /app/.venv .venv

WORKDIR /app
COPY src .
