#!/usr/bin/env bash
# exit on error
set -o errexit


echo "-> removing previous dump.json"
rm -f db-dump.json

echo "-> dumping sqlite to json"
python manage.py dumpdata --natural-foreign --natural-primary > db-dump.json

export DEBUG_USE_REMOTE_DB=1

echo "-> loading data to remote postgresql"
python manage.py loaddata db-dump.json

echo "-> removing previous dump.json"
rm -f db-dump.json