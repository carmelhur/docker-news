import os
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_CHANNEL = os.getenv("REDIS_CHANNEL")

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB  = os.getenv("MONGO_DB")
MONGO_COL = os.getenv("MONGO_COL")

TECH_KEYWORDS = [k.strip().lower() for k in os.getenv("TECH_KEYWORDS").split(",") if k.strip()]
PORT = int(os.getenv("PROCESSOR_PORT"))
