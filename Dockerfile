FROM --platform=linux/amd64 python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY backend/requirements-api.txt /tmp/requirements-api.txt
RUN pip install --no-cache-dir -r /tmp/requirements-api.txt

COPY backend/apps ./backend/apps
COPY backend/scripts/db_common.py ./backend/scripts/db_common.py
COPY data/raw/league_teams.json ./data/raw/league_teams.json
COPY data/raw/fixtures ./data/raw/fixtures
COPY data/analysis ./data/analysis
COPY ml/datasets ./ml/datasets

WORKDIR /app/backend
EXPOSE 8000

CMD ["sh", "-c", "uvicorn apps.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
