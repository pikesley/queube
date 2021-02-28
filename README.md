# Queube

![The Cube](assets/cube.gif)

## Installing it

From a box-fresh install of Raspberry Pi OS Lite via [NOOBS 3.5](https://www.raspberrypi.org/documentation/installation/noobs.md) (on a [Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/), which is probably important because this involves [Docker](https://en.wikipedia.org/wiki/Docker_(software))):

### Enable SSH

Login on the Pi's console and

```bash
sudo raspi-config nonint do_ssh 0
```

You should now be able to get on to the Pi with

```bash
ssh pi@raspberrypi.local
```

### Install the software

(Optionally) change the hostname:

```bash
sudo raspi-config nonint do_hostname queube
sudo reboot
```

You need `git`:

```bash
sudo apt-get install -y git
```

Then clone this repo:

```bash
git clone https://github.com/pikesley/queube
```

And install everything:

```bash
cd queube
make setup
```

## What is this?

The [Cube:Bit](https://shop.4tronix.co.uk/products/cubebit?variant=12698900889715) is basically a cube made out of 27 [ws2812 NeoPixels](https://learn.adafruit.com/adafruit-neopixel-uberguide) (I think), which can be driven with the [usual Python libs](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage). It presents itself as a 1-dimensional array of pixels, but this list wraps itself around physical space like some sort of [Peano Curve](https://en.wikipedia.org/wiki/Space-filling_curve) (which makes more sense when you look at how the layers are connected together).

The core of all this is the [Cube](cube.py). Its `#display` method takes data like this:

```python
[
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [255, 0, 0]],
    ],
    [
        [[0, 0, 0], [0, 255, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 255, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 255, 0], [0, 0, 0]],
    ],
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[255, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ],
]
```

which is 3, 3x3 layers of RGB colours, maps it onto the actual layout of the Cube, and turns on the lights.

### Running it locally

You can run it locally (with FakePixels for testing):

```bash
make build
make run
```

Then inside the container:

```bash
make
```

to run the tests

## There's a queue

There's also a [Redis](https://redis.io/) LIFO queue , with a [worker](worker.py) which picks JSON like this:

```json
{
  "data": ["3x3x3 RGB colours like the above"]
}
```

off of the `queube` queue and passes the `.data` to the Cube

## Driving it

There's some [Ruby in a Docker image](generators/frillsberry) called [frillsberry](https://www.thisworddoesnotexist.com/) which I wrote more than two years ago (when I was still writing Ruby every day for work) and I'm still trying to piece together exactly how it works, but basically it conjures up a 3-dimensional grid bigger than the Cube, with the Cube at the centre of it, picks a random starting point somewhere outside the Cube, creates a sphere of random radius centred on that point, colours it a random colour (with the intensity fading towards the outside), then fires it towards and through the centre of the Cube, lighting the pixels as it goes, creating a pretty light show.

Well, actually it does all this in the abstract, generating  a series of 3x3x3 grids of RGB colours, which it turns into JSON and pushes onto the queue.

The existence of this Ruby client is the main reason (other than over-engineering for the sake of it) that there's a queue in here and I'm not just hitting up the Python directly, tbh.

### Running it locally

You can run _this_ locally with:

```bash
cd generators/frillsberry
make build
make run
```

Then inside the container:

```bash
rake
```

to run the specs. There's a few things that can be usefully tuned in here, which I should really abstract out into some YAML or something.
