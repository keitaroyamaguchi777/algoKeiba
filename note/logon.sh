#!/bin/bash 
# source logon.sh
source ~/.bashrc 
workon venv
cd .virtualenvs/venv/
mysql-ctl start
