.PHONY: run

default: run

build-front:
	docker-compose build frontend

build:
	docker-compose build server

run:
	docker-compose up -d --force-recreate

dev-deps:
	docker-compose up -d --force-recreate db nginx frontend

dev:
	docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d --force-recreate

down:
	docker-compose down

local: dev-deps
	IS_DEBUG=TRUE POSTGRES_HOST=localhost POSTGRES_DB=mlpdb POSTGRES_USER=mlpuser POSTGRES_PASSWORD=mlppassword ./server/manage.py runserver

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
