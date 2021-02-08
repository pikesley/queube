#!/bin/bash

PI_EXISTS=$(sudo rabbitmqctl list_users | grep pio)

if [ ! "${PI_EXISTS}" ]
then
	sudo rabbitmqctl add_user pi raspberry
	sudo rabbitmqctl set_permissions -p / pi ".*" ".*" ".*"
fi
