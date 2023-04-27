#!/usr/bin/env bash

cd ..
docker-compose down
docker-compose up  -d db
sleep 10
docker-compose run django ./manage.py makemigrations aoi
#docker-compose run django ./manage.py makemigrations --empty aoi
#docker-compose run django ./manage.py makemigrations --empty user
#docker-compose up -d