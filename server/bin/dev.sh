#!/usr/bin/env bash
/usr/local/bin/python manage.py makemigrations --noinput
/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py collectstatic --noinput
/usr/local/bin/python manage.py runserver 0.0.0.0:8000
