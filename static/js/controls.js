lookups = {
    "active": "pause",
    "inactive": "play",
    "activating": "play",
    "deactivating": "pause"
}

var socket

$(document).ready(function () {
    socket = io(`ws://${location.hostname}:5000`);

    socket.on('phase', function (msg) {
        currentPhase = msg.data
        buttonContent = lookups[currentPhase]

        $('#control-button #button').html(buttons[buttonContent])
        $('#control-button').removeClass().addClass(currentPhase)

        $('#status').text(currentPhase)
    })

    socket.on('colour', function (msg) {
        $('h1').css('color', `rgb(${msg.data})`)
    })
});

function switchLights() {
    var disposition
    if (currentPhase == 'active') {
        disposition = 'inactive'
    }
    if (currentPhase == 'inactive') {
        disposition = 'active'
    }
    socket.emit('switch_lights', {
        data: disposition
    })
    return false
}
