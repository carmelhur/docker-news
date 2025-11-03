import os

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_CHANNEL = os.getenv("REDIS_CHANNEL")

FETCH_SECONDS = int(os.getenv("FETCH_SECONDS"))
NEWS_FEEDS = [u.strip() for u in os.getenv("NEWS_FEEDS", "").split(",") if u.strip()]
PORT = int(os.getenv("FETCHER_PORT"))
