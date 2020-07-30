#!/bin/bash

if [[ ! -f `pwd`'/../.env' ]]; then

    function get_random {
        base=$(openssl rand -base64 16)
        base_clear=${base/+//}
        base_clear=${base_clear////}
        base_clear=${base_clear//=/}
        echo $base_clear
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
