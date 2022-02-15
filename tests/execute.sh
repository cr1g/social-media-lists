#!/bin/bash

set -e

echo -e "\nStarting PostgreSQL database..."
docker-entrypoint.sh postgres &

sleep 5

echo -e "\Exporting required environment variables..."
export POSTGRES_HOST=localhost;
export POSTGRES_DB=${POSTGRES_DB};
export POSTGRES_PASSWORD=${POSTGRES_PASSWORD};
export POSTGRES_USER=${POSTGRES_USER};
export SECRET_KEY=secret-key;
export ACCESS_TOKEN_TTL_MINUTES=1000;
export REFRESH_TOKEN_TTL_MINUTES=5000;

echo -e "\nRunning tests..."
cd api && python3 manage.py test
