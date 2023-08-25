#!/usr/bin/env bash
#
sudo cp /home/ubuntu/luminar/gunicorn/gunicorn.socket /etc/systemd/gunicorn.socket
sudo cp /home/ubuntu/luminar/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
