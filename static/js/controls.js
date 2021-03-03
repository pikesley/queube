var neutral = "M18 18h-12c-3.311 0-6-2.689-6-6s2.689-6 6-6h12.039c3.293.021 5.961 2.701 5.961 6 0 3.311-2.688 6-6 6zm-6-10c2.208 0 4 1.792 4 4s-1.792 4-4 4-4-1.792-4-4 1.792-4 4-4z"
var paths = {
    "active": "M6 18h12c3.311 0 6-2.689 6-6s-2.689-6-6-6h-12.039c-3.293.021-5.961 2.701-5.961 6 0 3.311 2.688 6 6 6zm12-10c-2.208 0-4 1.792-4 4s1.792 4 4 4 4-1.792 4-4-1.792-4-4-4z",
    "inactive": "M18 18h-12c-3.311 0-6-2.689-6-6s2.689-6 6-6h12.039c3.293.021 5.961 2.701 5.961 6 0 3.311-2.688 6-6 6zm-12-10c2.208 0 4 1.792 4 4s-1.792 4-4 4-4-1.792-4-4 1.792-4 4-4z",
    "activating": neutral,
    "deactivating": neutral
}

var socket

$(document).ready(function () {
    socket = io(`http://${location.hostname}:5000`);

    socket.on('phase', function (msg) {
        currentPhase = msg.data

        $('#switch path').attr('d', paths[currentPhase])
        $('#switch').removeClass().addClass(currentPhase)
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
