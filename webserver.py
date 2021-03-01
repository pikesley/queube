import subprocess
from threading import Lock

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


def background_thread(desired_state):
    in_desired_state = False
    count = 0
    while not in_desired_state:
        state = lights_state()
        in_desired_state = state == desired_state
        socketio.sleep(0.5)
        count += 1
        socketio.emit("response", {"data": f"{state}, {count}"})


@app.route("/")
def index():
    return render_template("index.html", async_mode=socketio.async_mode)


@socketio.event
def switch_lights(desired_state):
    lookups = {
        "on": {"command-arg": "start", "expectation": "active"},
        "off": {"command-arg": "stop", "expectation": "inactive"},
    }

    params = lookups[desired_state["data"]]
    subprocess.Popen(["sudo", "service", "frillsberry", params["command-arg"]])

    global thread
    with thread_lock:
        thread = socketio.start_background_task(
            background_thread(params["expectation"])
        )

@socketio.event
def connect():
    socketio.emit("response", {"data": lights_state()})

def lights_state():
    check = subprocess.run(
        "systemctl is-active frillsberry".split(), capture_output=True
    )
    return check.stdout.decode("utf-8").strip()


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)
