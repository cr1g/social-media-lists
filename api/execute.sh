#!/bin/bash

set -e

echo -e "\nWait for database startup.."
sleep 5

echo -e "\nApplying database migrations..."
python manage.py migrate

echo -e "\nCollecting static files..."
python manage.py collectstatic --noinput

if [[ $ENVIRONMENT = "dev" ]]; then
  echo -e "\nRunning development server..."
  python manage.py runserver 0.0.0.0:$API_PORT
else
  echo -e "\nRunning server using gunicorn..."
  gunicorn --workers 2 --worker-class gevent --bind 0.0.0.0:$API_PORT --access-logfile - --error-logfile - b4y.wsgi
fi
