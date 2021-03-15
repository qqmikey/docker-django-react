#!/usr/bin/env bash
/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py collectstatic --noinput
/usr/local/bin/gunicorn backend.asgi:application -w 1 -b :8000 -k uvicorn.workers.UvicornWorker
/bin/bash
