#!usr/bin/env bash
# exit or error

set -o errexit

pip install -r requirements.txt

# run the application
cd backend
python manage.py makemigrations
python manage.py migrate
