#!/usr/bin/env bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn backend.asgi:application -w 1 -b :8000 -k uvicorn.workers.UvicornWorker
