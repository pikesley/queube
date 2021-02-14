import json
import subprocess

import pika


def turn_on():
    """Turn everything on."""
    start_service()


def turn_off():
    """Turn everything off."""
    stop_service()
    turn_off_the_lights()


def start_service():
    """Start the frillsberry service."""
    subprocess.run("service frillsberry start".split(), check=True)


def stop_service():
    """Stop the frillsberry service."""
    subprocess.run("service frillsberry stop".split(), check=True)


def turn_off_the_lights():
    """Set the lights to off."""
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    queue = "queube"

    channel = connection.channel()
    channel.queue_declare(queue=queue)
    black = [[[0, 0, 0]] * 9] * 3
    data = json.dumps({"data": black})
    channel.basic_publish(exchange="", routing_key=queue, body=data)
