from flask import Flask, json
import redis

r = redis.Redis()
api = Flask(__name__)

@api.route('/increment', methods=['GET'])
def get_id():
  # read from redis and increment number
  num = r.incr("numberstore")
  # build json
  id = {"id": num}
  # return json
  return json.dumps(id)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=80)