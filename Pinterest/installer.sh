#!/bin/bash

apt-get update
apt-get upgrade

sudo apt install vim
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo pip install virtualenv
sudo apt-get install chromium-chromedriver
sudo apt-get -y install fbi

sudo apt-get update

python3 -m venv venv
source ./venv/bin/activate

pip3 install -r requirements.txt