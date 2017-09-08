#!/bin/sh
python manage.py showmigrations

python3 manage.py makemigrations sampling
python3 manage.py migrate

