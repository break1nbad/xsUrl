##!/usr/bin/env bash
## exit on error
#set -o errexit
#

#python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate
#python manage.py coll --no-input
