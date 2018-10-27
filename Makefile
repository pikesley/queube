apt:
	sudo apt-get install -y rabbitmq-server

cubebit:
	curl -sS https://get.pimoroni.com/unicornhat | bash
	curl -sS http://4tronix.co.uk/cb.sh | bash

install:
	sudo pip3 install -r requirements.txt

.PHONY: systemd
systemd:
	sudo systemctl enable /home/pi/Queube/etc/systemd/queube-worker.service
	sudo service queube-worker restart

env:
	@echo QUEUE=queube > /home/pi/.env
