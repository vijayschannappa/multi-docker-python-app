#import pandas as pd
from flask import Flask
import redis


r = redis.Redis(host='redis-server',port = 6379)
r.set('visits',0)

app = Flask(__name__)
app.config["DEBUG"] = True
    
@app.route('/',methods=['GET'])
def check_for_status():
    return 'app is up and running'

@app.route('/check/', methods=['GET'])
def check_flask():
    total_visits=fetch_and_update_redis_table()
    return f"number of visits:{total_visits}"

def fetch_and_update_redis_table():
    total_visits=r.get('visits')
    r.set('visits',int(total_visits)+1)
    return total_visits

if __name__ == "__main__":
    app.run(host='0.0.0.0')