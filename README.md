This project is a system that gets tech news and shows them on a simple web page.
It has three FastAPI apps: fetcher, processor, and frontend, all running in Docker with Redis and MongoDB.

The fetcher reads RSS feeds (like BBC Tech or NYTimes Tech). RSS is a news format that gives headlines and links. The fetcher runs every few minutes, takes each article’s link, and sends it to Redis.

The processor listens to Redis, gets each link, and checks if it’s about technology. It uses a list of tech words like “ai”, “cloud”, “docker”, “linux”. If it fits, it saves the link in MongoDB. The upsert=True makes sure no duplicate articles are saved.

The frontend connects to MongoDB and shows all saved links on a web page.
When you open http://localhost:8000/articles, you see a list of blue clickable links that open the real articles.

Everything runs together with Docker Compose.
All services use one network (news_net) so they can talk to each other.
MongoDB uses a volume (mongo_data) so data stays after restart.
Settings like fetch time, feed URLs, and keywords are in a .env file.
