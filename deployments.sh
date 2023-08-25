#!/bin/sh     
git pull origin master
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
sudo systemctl restart nginx
sudo systemctl restart gunicorn
