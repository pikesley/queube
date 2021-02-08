import json

import pika

from cube import Cube

QUEUE = "queube"

cube = Cube()

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)


def callback(_, __, ___, body):
    """Do something with the data."""
    try:
        data = json.loads(body.decode("utf-8"))
        cube.display(data["data"])
    except TypeError:
        print("Your data is bad")


channel.basic_consume(QUEUE, callback)

print(" [*] Waiting for jobs")
channel.start_consuming()
