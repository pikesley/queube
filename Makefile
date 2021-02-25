PROJECT = $(shell basename $$(pwd))
ID = pikesley/${PROJECT}
PIHOST = queube.local

default: all

# Laptop targets

build: laptop-only
	docker build \
		--tag ${ID} .

run: laptop-only
	docker run \
		--interactive \
		--tty \
		--name ${PROJECT} \
		--volume $(shell pwd):/opt/${PROJECT} \
		--volume ${HOME}/.ssh:/root/.ssh \
		--rm \
		${ID} bash

# Docker targets

all: docker-only format lint test clean

black: docker-only
	python -m black .

isort: docker-only
	python -m isort .

format: docker-only black isort

lint: docker-only
	python -m pylama

test: docker-only
	python -m pytest \
		--random-order \
		--verbose \
		--capture no \
		--failed-first \
		--exitfirst \
		--cov

clean: docker-only
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;
	@find . -depth -name ".coverage.*" -exec rm {} \;

dev-install: docker-only
	 python -m pip install -r requirements-dev.txt

push-code: docker-only clean
	rsync -av /opt/${PROJECT} pi@${PIHOST}:

# Pi targets

setup: pi-only set-python apt-installs config-redis install frillsberry install-systemd

install: pi-only
	sudo python -m pip install -r requirements.txt

set-python: pi-only
	sudo update-alternatives --install /usr/local/bin/python python /usr/bin/python2 1
	sudo update-alternatives --install /usr/local/bin/python python /usr/bin/python3 2

apt-installs: pi-only
	sudo apt-get update
	sudo apt-get install -y redis docker.io python3-pip

config-redis:
	sudo cat /etc/redis/redis.conf | sed "s/bind 127.0.0.1 ::1/#bind 127.0.0.1 ::1/" | sed "s/protected-mode yes/protected-mode no/" > /tmp/redis.conf
	sudo mv /tmp/redis.conf /etc/redis/redis.conf

install-systemd: pi-only
	sudo systemctl enable -f /home/pi/queube/etc/systemd/queube-worker.service
	sudo systemctl enable -f /home/pi/queube/etc/systemd/frillsberry.service

	sudo service redis-server restart
	sudo service queube-worker restart
	sudo service frillsberry restart

frillsberry:
	bash scripts/build-frillsberry.sh

# Guardrails

docker-only:
	@if ! [ "$(shell uname -a | grep 'x86_64 GNU/Linux')" ] ;\
	then \
		echo "This target can only be run inside the container" ;\
		exit 1 ;\
	fi

laptop-only:
	@if ! [ "$(shell uname -a | grep 'Darwin')" ] ;\
	then \
		echo "This target can only be run on the laptop" ;\
		exit 1 ;\
	fi

pi-only:
	@if ! [ "$(shell uname -a | grep 'armv.* GNU/Linux')" ] ;\
	then \
		echo "This target can only be run on the Pi" ;\
		exit 1 ;\
	fi
