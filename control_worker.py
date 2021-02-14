import json

import pika

from light_control import turn_off, turn_on

QUEUE = "control"


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)


def callback(_, __, ___, body):
    """Do something with the data."""
    try:
        data = json.loads(body.decode("utf-8"))
        if data["state"] == "off":
            turn_off()

        if data["state"] == "on":
            turn_on()

    except KeyError:
        print("Your data is bad")

    except TypeError:
        print("Your data is bad")


channel.basic_consume(QUEUE, callback)

print(" [*] Waiting for jobs")
channel.start_consuming()
