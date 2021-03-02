import json
import os
from time import sleep

import redis

from cube import Cube

# r = redis.Redis(host="192.168.68.105")  # get this from env
def do_lights(stack):
    for item in reversed(stack):
        try:
            cube.display(item)
        except TypeError:
            print("Your data is bad")
        finally:
            sleep(0.05)


r = redis.Redis(host=os.environ["REDIS"])

cube = Cube()

while True:
stack = []
    data = r.lpop("lights")

    if data:
        try:
            item = json.loads(data.decode("utf-8"))["data"]
            if item == "EOF":
                do_lights(stack)
                stack = []
            else:
                stack.append(item)

        except Exception:
            pass

    else:
        sleep(1)

