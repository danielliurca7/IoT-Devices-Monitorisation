# IoT Devices Monitorization
Application that collects data from virtual IoT devices, stores them in a database and offers the possibility of visualization, using microservices.

## MQTT Broker
As a message queue we use an image that implements the MQTT protocol. All the messages pass through this queue and are parsed by an adaptor.

## Adaptor Service
A service that consumes messages from the queue and stores them to the database.

## InfluxDB Database
InfluxDB is a time series database and it is used because there is an need in retain data by timestamp, in order to observe the evolution of a measure over time.

## Grafana
In order to visualize the data a Grafana image is used, offering the ability to observe the evolution in time of a measure on a specific device.

## IoT Devices
For simplicity, the IoT Devices are going to be simulated. Thus we have a client that puts random data in a certain ranges in the queue.
