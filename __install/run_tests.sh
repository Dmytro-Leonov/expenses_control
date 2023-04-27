#!/usr/bin/env bash

cd ..
docker-compose down
set -e
docker-compose -f docker-compose-test.yml down -v
docker-compose -f docker-compose-test.yml up -d pgdb
sleep 5

#docker-compose -f docker-compose-test.yml run webapplication ./manage.py test publisher.tests.WrongDatesTestCase --noinput
#docker-compose -f docker-compose-test.yml run webapplication ./manage.py test --noinput
#docker-compose -f docker-compose-test.yml exec webapplication ./manage.py test --keepdb
#docker-compose -f docker-compose-test.yml up -d --remove-orphans

docker-compose -f docker-compose-test.yml run django ./manage.py test user.tests.UserTestCase --noinput --traceback --keepdb

#docker-compose -f docker-compose-test.yml down -v