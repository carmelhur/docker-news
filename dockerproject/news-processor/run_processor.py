import asyncio, json, redis
from pymongo import MongoClient, ASCENDING
from fastapi import FastAPI
from config import (
    REDIS_HOST, REDIS_PORT, REDIS_CHANNEL,
    MONGO_URL, MONGO_DB, MONGO_COL,
    TECH_KEYWORDS
)

svc = FastAPI(title="news-processor")

def col():
    c = MongoClient(MONGO_URL)
    collection = c[MONGO_DB][MONGO_COL]
    collection.create_index([("url", ASCENDING)], unique=True)
    return collection

@svc.get("/health")
def health():
    return {"status": "ok"}

@svc.on_event("startup")
async def start_worker():
    collection = col()
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    p = r.pubsub()
    p.subscribe(REDIS_CHANNEL)

    async def loop():
        for msg in p.listen():
            if msg.get("type") != "message":
                await asyncio.sleep(0)
                continue
            try:
                article = json.loads(msg["data"])
                url = article.get("url")
                title = article.get("title", "").lower()
                summary = article.get("summary", "").lower()
                text = f"{title} {summary}"
                is_tech = any(word in text for word in TECH_KEYWORDS)
                if is_tech and url and url.startswith("http"):
                    collection.update_one(
                        {"url": url},
                        {"$set": {
                            "url": url,
                            "title": article.get("title", ""),
                            "summary": article.get("summary", "")
                        }},
                        upsert=True
                    )

            except Exception:
                continue

            await asyncio.sleep(0)

    asyncio.create_task(loop())
