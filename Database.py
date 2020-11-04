import redis
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.r = redis.from_url(os.environ.get("REDIS_URL"))
