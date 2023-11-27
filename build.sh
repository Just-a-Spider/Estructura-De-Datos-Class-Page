#!usr/bin/env bash
# exit or error

set -o errexit

pip install -r requirements.txt

# run the application
python backend/manage.py makemigrations exercises 
python backend/manage.py migrate
python backend/manage.py loaddata whole.json

cd backend