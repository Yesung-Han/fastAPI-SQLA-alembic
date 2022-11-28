#!/bin/bash

pip install -r requirements-dev.txt
# python manage.py collectstatic --noinput

# python -m celery -A lims.celery worker --loglevel=DEBUG -E -c 1 &
# python -m uvicorn lims.asgi:application --reload --host 0.0.0.0 --port 8080

python app/backend_pre_start.py

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080