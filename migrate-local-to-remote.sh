#!/usr/bin/env bash
# exit on error
set -o errexit


echo "-> make migrations"
python manage.py makemigrations

echo "-> removing previous dump.json"
rm -f db-dump.json

export DEBUG_USE_REMOTE_DB=1
echo "-> make migrations"
python manage.py migrate
