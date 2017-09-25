#!/bin/bash 
# source logon.sh
export WORKON_HOME=/home/ubuntu/workspace/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon venv
cd .virtualenvs/venv/
mysql-ctl start

python manage.py runserver $IP:$PORT
