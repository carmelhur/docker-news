import os
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB  = os.getenv("MONGO_DB")
MONGO_COL = os.getenv("MONGO_COL")
PORT = int(os.getenv("FRONTEND_PORT"))
