#!/usr/bin/env bash
apt-get update
apt-get install -y python-pip
pip install -U pip setuptools
cd /home/vagrant/order-tracker/src
sudo pip install -r requirements.txt
python manage.py migrate
# python manage.py runserver 0.0.0.0:8000
# acessivel em 192.168.33.11
