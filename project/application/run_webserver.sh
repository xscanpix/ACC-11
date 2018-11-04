#!/bin/sh

# Configure rabbitmq
rabbitmqctl add_user rabbit rabbit
rabbitmqctl set_permissions -p / rabbit ".*" ".*" ".*"
rabbitmqctl set_user_tags rabbit administrator

# Configure redis
cat ./app/config/redis.conf > /etc/redis/redis.conf
service redis-server restart

cd ./app
flask run --host=0.0.0.0 &