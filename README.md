# Queube

_Processing the queued data from [CubeREST](https://github.com/pikesley/CubeREST) to make the lights come on_

## Installation

On a fresh, clean [Raspbian](https://www.raspbian.org/) install (which should already have Python 3), try the following handy `make` targets

### `make apt`

* installs `rabbitmq-server`

### `make cubebit`

* installs the [NeoPixel and Cube:Bit Python libs](https://4tronix.co.uk/blog/?p=1827)

### `make install`

* installs from `requirements.txt`

### `make systemd`

* installs the `systemd` start-up script - this target relies on this all being checked-out at `/home/pi/Queube` - then starts the service

### `make env`

Sets up the shared `.env` file with the queue name we'll use for RabbitMQ

## What is this even for?

The [Cube:Bit](https://4tronix.co.uk/blog/?p=1770), in common with most Raspberry Pi hardware, comes with Python drivers. I don't really like Python, so I wrote my [front-end in Ruby](https://github.com/pikesley/CubeREST) and am using the minimum amount of Python I could get away with to actually operate the lights

So this sets up a RabbitMQ consumer, which pulls off the data sent down from the API, reorders the list (because the pixels in the Cube:Bit are ordered strangely), then lights the lights
