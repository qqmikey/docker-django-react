#!/usr/bin/env bash
/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py collectstatic --noinput
/usr/local/bin/gunicorn backend.wsgi:application -w 1 -b :8000
/bin/bash
