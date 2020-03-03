import os
import logging
import json
import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
from datetime import datetime


def on_connect(client, userdata, flags, rc):
    logging.info('Connected with result code {}'.format(rc))

    client.subscribe('#')


def on_message(client, userdata, msg):
    logging.info('Received a message by topic [{}]'.format(msg.topic))

    location, device = tuple(msg.topic.split('/'))

    data = json.loads(msg.payload)

    time = datetime.fromisoformat(data['timestamp']) if 'timestamp' in data else datetime.now()
    logging.info('Datastamp is ' + ('NOW' if 'timestamp' not in data else data['timestamp'].split('T')[0] + ' ' + data['timestamp'].split('T')[1]))

    measurement_list = []

    for label in {k : v for k, v in data.items() if type(v) is int or type(v) is float}:
        measurement_list.append({
            'measurement': location,
            'tags' : {
                'device' : device,
                'label'  : label
            },
            'time': time,
            'fields' : {
                'value': float(data[label])
            }
        })

        logging.info('.'.join([location, device, label]) + ' ' + str(data[label]))

    influx_client.write_points(measurement_list, time_precision='ms')



if os.environ['DEBUG_DATA_FLOW'] == "true":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

influx_client = InfluxDBClient(host='influx', port=8086, database='IoT_DB')

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect('broker', 1883, 60)

mqtt_client.loop_forever()