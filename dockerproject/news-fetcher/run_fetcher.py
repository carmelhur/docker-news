import asyncio, json, feedparser, redis
from fastapi import FastAPI
from config import NEWS_FEEDS, FETCH_SECONDS, REDIS_HOST, REDIS_PORT, REDIS_CHANNEL

svc = FastAPI(title="news-fetcher")

def fetch_once():
    articles = []
    for feed_url in NEWS_FEEDS:
        parsed = feedparser.parse(feed_url)
        for e in parsed.entries[:5]:
            link = e.get("link")
            title = e.get("title", "")
            summary = e.get("summary", "")
            if link:
                articles.append({
                    "url": link,
                    "title": title,
                    "summary": summary
                })
    return articles


@svc.get("/health")
def health():
    return {"status": "ok"}

@svc.on_event("startup")
async def startup_task():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    async def loop():
        while True:
            for article in fetch_once():
                r.publish(REDIS_CHANNEL, json.dumps(article))
            await asyncio.sleep(FETCH_SECONDS)

    asyncio.create_task(loop())
