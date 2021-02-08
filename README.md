# Queube

## Installing it

From a box-fresh install of Raspberry Pi OS Lite via [NOOBS 3.5](https://www.raspberrypi.org/documentation/installation/noobs.md):

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
