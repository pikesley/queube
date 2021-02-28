import json
from time import sleep
import os

import redis

from cube import Cube

# r = redis.Redis(host="192.168.68.105")  # get this from env
r = redis.Redis(host=os.environ["REDIS"])

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

        finally:
            sleep(0.05)  # put this in config

    else:
        sleep(1)
