from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pymongo import MongoClient
from config import MONGO_URL, MONGO_DB, MONGO_COL

svc = FastAPI(title="news-frontend")

def collection():
    return MongoClient(MONGO_URL)[MONGO_DB][MONGO_COL]

@svc.get("/health")
def health():
    return {"status": "ok"}

@svc.get("/articles", response_class=HTMLResponse)
def list_urls():
    docs = collection().find({}, {"_id": 0, "url": 1}).sort([("_id", -1)])
    urls = [d["url"] for d in docs if d.get("url") and d["url"].startswith("http")]

    html = """
    <html>
      <head>
        <meta charset="utf-8"/>
        <title>News Links</title>
        <style>
          body { font-family: Arial; margin: 30px; background: #fafafa; }
          h2 { color: #0078D7; }
          a { color: #0078D7; text-decoration: none; }
          a:hover { text-decoration: underline; }
          div { margin-bottom: 8px; }
        </style>
      </head>
      <body>
        <h2>News Links</h2>
    """
    for u in urls:
        html += f"<div><a href='{u}' target='_blank'>{u}</a></div>\n"
    html += """
      </body>
    </html>
    """
    return html
