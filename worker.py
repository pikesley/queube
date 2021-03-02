import json
import os
import signal
from time import sleep

import redis

from cube import Cube

run = True


def handle_stop_signals(signum, frame):
    global run
    run = False


signal.signal(signal.SIGTERM, handle_stop_signals)


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

stack = []
while run:
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

r.flushall()
