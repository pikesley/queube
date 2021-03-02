import json
import os
import signal
from time import sleep

import redis

from cube import Cube

RUN = True


def handle_stop_signals(_, __):
    """Intercept SIGTERM and shutdown gracefully."""
    # https://stackoverflow.com/a/41753517
    global RUN  # pylint:disable=W0603
    RUN = False


signal.signal(signal.SIGTERM, handle_stop_signals)


def do_lights(colours):
    """Actually light the lights."""
    for frame in reversed(colours):
        try:
            cube.display(frame)
        except TypeError:
            print("Your data is bad")
        finally:
            sleep(0.05)


r = redis.Redis(host=os.environ["REDIS"])

cube = Cube()

stack = []
while RUN:
    data = r.lpop("lights")

    if data:
        try:
            item = json.loads(data.decode("utf-8"))["data"]
            if item == "EOF":
                do_lights(stack)
                stack = []
            else:
                stack.append(item)

        except json.decoder.JSONDecodeError:
            print("Your data is bad")

    else:
        sleep(1)

r.flushall()
