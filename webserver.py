import json
import subprocess

import pika
from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route("/", methods=["GET"])
def index():
    """Show the front page."""
    return {"status": "OK"}, 200


@app.route("/lights", methods=["POST", "PATCH"])
def control_lights():
    """Control the lights."""
    if not request.content_length:
        return {"error": "No data"}, 422

    app.data = request.get_json()
    if "state" not in app.data:
        return {"error": "Bad data"}, 422

    enqueue_control_job(app.data)
    return {"status": "OK"}, 200


@app.route("/lights", methods=["GET"])
def get_lights():
    """Get the lights status."""
    check = subprocess.Popen("systemctl is-active --quiet frillsberry".split())
    status = check.wait()

    if status == 0:
        return {"lights": "on"}, 200

    return {"lights": "off"}, 200


def enqueue_control_job(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    QUEUE = "control"
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE)
    channel.basic_publish(exchange="", routing_key=QUEUE, body=json.dumps(data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
