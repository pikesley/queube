import json

import redis

from cube import Cube

r = redis.Redis(host="192.168.68.105")

cube = Cube()

while True:
    data = r.lpop("lights")
    if data:
        data = data.decode("utf-8")
        data = json.loads(data)
        try:
            cube.display(data["data"])
        except TypeError:
            print("Your data is bad")
