build:
    docker swarm init
    docker build ./Adaptor/ -t adaptor

start: build
    docker stack deploy -c stack.yml sprc3
    py ./"IoT Device"/device.py

stop:
    docker stack rm sprc3

clear: stop
    docker rmi adaptor
    docker volume rm sprc3_timeseries_data
    