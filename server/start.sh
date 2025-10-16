#!/bin/bash

redis-server --daemonize yes

python manage.py collectstatic --noinput

python manage.py makemigrations
python manage.py migrate

celery -A main beat -l INFO &> qcluster.log &
celery -A main worker -l INFO &> worker.log &

python manage.py runserver 0.0.0.0:8000 