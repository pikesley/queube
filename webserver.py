import json
import os
import subprocess
from threading import Lock

import redis
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

ASYNC_MODE = None

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode=ASYNC_MODE, cors_allowed_origins="*")

app.state_thread = None
app.state_thread_lock = Lock()

app.colour_thread = None
app.colour_thread_lock = Lock()

app.redis = redis.Redis(host=os.environ["REDIS"])
app.current_colour = None


def state_thread(params):
    """Monitor and report the state of a process."""
    in_desired_state = False
    while not in_desired_state:
        state = service_state(params["service"])
        in_desired_state = state == params["expectation"]
        socketio.emit("state", {"data": state})
        socketio.sleep(0.5)


def colour_thread():
    """Send the background colour."""
    while True:
        try:
            colour = json.loads(app.redis.get("current-colour"))
            if not colour == app.current_colour:
                app.current_colour = colour
                socketio.emit("colour", {"data": app.current_colour})
        except TypeError:
            pass

        socketio.sleep(1)


@socketio.event
def switch_lights(desired_state):
    """Switch the lights on or off."""
    lookups = {
        "active": {
            "service": "frillsberry",
            "command-arg": "start",
            "phase": "activating",
            "expectation": "active",
        },
        "inactive": {
            "service": "queube-worker",
            "command-arg": "stop",
            "phase": "deactivating",
            "expectation": "inactive",
        },
    }

    params = lookups[desired_state["data"]]

    socketio.emit("phase", {"data": params["phase"]})
    subprocess.Popen(["sudo", "service", params["service"], params["command-arg"]])
    with app.state_thread_lock:
        app.thread = socketio.start_background_task(state_thread(params))

    socketio.emit("phase", {"data": params["expectation"]})


@socketio.event
def connect():
    """Make first connection to the client."""
    socketio.emit("phase", {"data": service_state("queube-worker")})
    with app.colour_thread_lock:
        app.colour_thread = socketio.start_background_task(colour_thread)


def service_state(service):
    """Report the status of a systemd service."""
    check = subprocess.run(  # pylint:disable=W1510
        ["systemctl", "is-active", service], capture_output=True
    )
    return check.stdout.decode("utf-8").strip()


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
