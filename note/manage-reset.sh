#!/bin/sh 
cd /home/ubuntu/workspace/.virtualenvs/venv
mysql-ctl start
source logon.sh

mysql -uroot -padmin keibadb -e "drop table sampling_bangumi;"
mysql -uroot -padmin keibadb -e "drop table sampling_kishu_sabun;"
mysql -uroot -padmin keibadb -e "drop table sampling_kyousouba;"
mysql -uroot -padmin keibadb -e "drop table sampling_kyousouba_extend;"
mysql -uroot -padmin keibadb -e "drop table sampling_chokuzen;"
mysql -uroot -padmin keibadb -e "drop table sampling_uma_kihon;"
mysql -uroot -padmin keibadb -e "drop table sampling_zensou;"
mysql -uroot -padmin keibadb -e "delete from django_migrations where app='sampling';"
python manage.py migrate
