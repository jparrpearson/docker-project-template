import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)

@app.route("/")
def hello():
    return "Hello World from Python!"

@app.route("/count")
def count():
    return "Count: %d" % cache.incr("count")
