#!/usr/bin/env bash
# exit on error
set -o errexit


#echo "-> make migrations"
#python manage.py makemigrations

#echo "-> removing previous dump.json"
#rm -f db-dump.json

export DEBUG_USE_REMOTE_DB=1
echo "-> make migrations"
python manage.py makemigrations
echo "-> make migrate"
python manage.py migrate

#export DJANGO_SUPERUSER_USERNAME="z0rge"
#export DJANGO_SUPERUSER_PASSWORD="15nZuZw@sted//??"
#export DJANGO_SUPERUSER_EMAIL="axelfx13@gmail.com"
#python manage.py createsuperuser --noinput