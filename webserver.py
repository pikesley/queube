import subprocess
from threading import Lock

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

ASYNC_MODE = None

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode=ASYNC_MODE, cors_allowed_origins="*")
app.thread = None
thread_lock = Lock()


def background_thread(params):
    """Monitor and report the state of a process."""
    in_desired_state = False
    while not in_desired_state:
        state = service_state(params["service"])
        in_desired_state = state == params["expectation"]
        socketio.emit("response", {"data": state})
        socketio.sleep(0.5)


@socketio.event
def switch_lights(desired_state):
    """Switch the lights on or off."""
    lookups = {
        "on": {
            "service": "frillsberry",
            "command-arg": "start",
            "expectation": "active",
        },
        "off": {
            "service": "queube-worker",
            "command-arg": "stop",
            "expectation": "inactive",
        },
    }

    params = lookups[desired_state["data"]]
    subprocess.Popen(["sudo", "service", params["service"], params["command-arg"]])

    with thread_lock:
        app.thread = socketio.start_background_task(background_thread(params))


@socketio.event
def connect():
    """Make first connection to the client."""
    socketio.emit("response", {"data": service_state("queube-worker")})


def service_state(service):
    """Report the status of a systemd service."""
    check = subprocess.run(  # pylint:disable=W1510
        ["systemctl", "is-active", service], capture_output=True
    )
    return check.stdout.decode("utf-8").strip()


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)
