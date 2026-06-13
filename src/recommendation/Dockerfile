FROM python:3.12-slim-bookworm AS base
WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "recommendation_server.py"]