#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser_if_none_exists --user=gleon --password=changeme --email=gleon@savingl.cl