.PHONY: run

default: run

production_compose_files = -f docker-compose.yml
compose_files = $(production_compose_files) -f docker-compose-dev.yml

define set_default_container
	ifndef c
	c = backend
	else ifeq (${c},all)
	override c=
	endif
endef

define use_env
	include .env
#	export
endef


set-container:
	$(eval $(call set_default_container))

build: set-container
	docker-compose $(compose_files) build ${c}

run:
	docker-compose $(production_compose_files) up -d --force-recreate ${c}

dev:
	docker-compose $(compose_files) up -d --force-recreate ${c}

restart: set-container
	docker-compose $(compose_files) restart ${c}

stop: set-container
	docker-compose $(compose_files) stop ${c}

down:
	docker-compose $(compose_files) down

exec: set-container
	docker-compose $(compose_files) exec ${c} /bin/bash

log: set-container
	docker-compose $(compose_files) logs -f ${c}

ps:
	docker-compose $(compose_files) ps


#run backend local
dev-local-deps:
	docker-compose $(compose_files) up -d --force-recreate db nginx frontend

python_path = backend/venv/bin/
local: dev-local-deps
	$(eval $(call use_env))
	. $(python_path)activate && IS_DEBUG=TRUE POSTGRES_HOST=localhost POSTGRES_DB=${POSTGRES_DB} \
	POSTGRES_USER=${POSTGRES_USER} POSTGRES_PASSWORD=${POSTGRES_PASSWORD} ./backend/manage.py runserver


nginx-test:
	docker-compose $(production_compose_files) exec nginx nginx -t

nginx-reload:
	docker-compose $(production_compose_files) exec nginx nginx -s reload

makemigrations:
	docker-compose $(production_compose_files) exec backend ./manage.py makemigrations

migrate: makemigrations
	docker-compose $(production_compose_files) exec backend ./manage.py migrate

collectstatic:
	docker-compose $(production_compose_files) exec backend ./manage.py collectstatic --noinput
	docker-compose $(production_compose_files) exec backend ./manage.py clear_templates_cache

clear-static:
	sudo rm -rf frontend/build/*
	sudo rm -rf frontend/dist/*
	sudo rm -rf backend/static/*

build-static:
	docker-compose $(production_compose_files) up --force-recreate frontend

frontend: build-static collectstatic
