#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install git mpd mpc python-pyudev python-mpd -y
sudo mkdir /mnt/usb/

git clone https://github.com/MrZoidberg/RPi-OBABP.git
