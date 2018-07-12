.PHONY: run

default: run

build:
	docker-compose build

run:
	docker-compose up -d --force-recreate

dev:
	docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d --force-recreate

exec:
	docker-compose exec server /bin/bash

makemigrations:
	docker-compose exec server ./manage.py makemigrations

migrate: makemigrations
	docker-compose exec server ./manage.py migrate

log:
	docker-compose logs -f server

collectstatic:
	docker-compose exec server ./manage.py collectstatic --noinput

exec-front:
	docker-compose exec frontend /bin/bash

build-static:
	docker-compose up --force-recreate frontend

frontend: build-static collectstatic
