#!/usr/bin/env bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/luminar/nginx/nginx.conf /etc/nginx/sites-available/luminar 
sudo ln -s /etc/nginx/sites-available/luminar /etc/nginx/sites-enabled/

sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx
