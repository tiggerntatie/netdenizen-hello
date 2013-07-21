import os
from flask import Flask
import redis

app = Flask(__name__)

def getredis():
    redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
    return redis.from_url(redis_url)

@app.route('/')
def hello():
    return 'Hello World of Wonder and Delight!'

@app.route('/test')
def test():
    return os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

@app.route('/set')
def set():
    r = getredis()
    r.set('varname', 1001)
    return 'We have set "varname" to 1001'

@app.route('/get')
def get():
    r = getredis()
    return str(r.get('varname'))

@app.route('/save')
def save():
    r = getredis()
    r.save()
    return 'r.save executed OK'
