#!/bin/bash

if [[ ! -f `pwd`'/../.env' ]]; then

    function get_random {
        echo `openssl rand -base64 16`
    }

    touch `pwd`'/.env'
    echo "SECRET_KEY=$(get_random)
POSTGRES_DB=$(get_random)
POSTGRES_USER=$(get_random)
POSTGRES_PASSWORD=$(get_random)
POSTGRES_HOST=db
POSTGRES_PORT=5432" > `pwd`'/.env'
fi

echo 'Done.'