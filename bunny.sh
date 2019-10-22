#!/bin/sh
( sleep 45 ; \

rabbitmqctl -n rabbit@bunny1 add_user user user
rabbitmqctl set_permissions -p / user  ".*" ".*" ".*" ) &

exec docker-entrypoint.sh rabbitmq-server $@