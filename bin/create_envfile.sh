#!/bin/bash

if [[ ! -f $(pwd)'/.env' ]]; then

  function create_random() {
    echo $(LC_CTYPE=C tr -dc a-z0-9_ </dev/urandom | head -c 16)
  }

  function create_secret_key() {
    echo $(LC_CTYPE=C tr -dc "A-Za-z0-9@#$%^&*-+_=()" </dev/urandom | head -c 52)
  }

  echo 'create .env file...'

  touch $(pwd)'/.env'
  echo "
# postgres db
POSTGRES_DB=$(create_random)
POSTGRES_USER=$(create_random)
POSTGRES_PASSWORD=$(create_random)

POSTGRES_HOST=db
POSTGRES_PORT=5432

# backend
SECRET_KEY=$(create_secret_key)
JWT_SECRET_KEY=$(create_secret_key)
" >$(pwd)'/.env'
fi

echo 'Done.'
