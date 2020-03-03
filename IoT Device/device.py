import time
import logging
import json
import paho.mqtt.client as mqtt
from random import randint, uniform

device_name = ['UPB/RPi_1', 'UPB/Gas', 'UPB/Mongo', 'Regie/Cherry']

def on_connect(client, userdata, flags, rc):
    print('Connected with result code {}'.format(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)
client.loop_start()



while True:
    data = [
        {
            'BAT'    : randint(70, 100) ,
            'HUM'    : round(uniform(30, 50), 2) ,
            'PRJ'    : 'SPRC' ,
            'TMP'    : round(uniform(16, 30), 2) ,
            'status' : "OK"
        }, {
            'BAT' : randint(50, 70) ,
            'CO'  : round(uniform(60, 70), 2) ,
            'HUM' : round(uniform(30, 50), 2) ,
            'NO2' : round(uniform(0.08, 0.11), 2) ,
            'O2'  : round(uniform(11.5, 12), 2) ,
            'TC'  : round(uniform(18.3, 18.7), 2)
        }, {
            'BAT' : randint(40, 80),
            'HUM' : round(uniform(80, 100), 2),
            'TC'  : round(uniform(1.3, 1.7), 2)
        }, {
            'BAT' : randint(50, 70) ,
            'CO'  : round(uniform(62, 75), 2) ,
            'NO2' : round(uniform(0.09, 0.12), 2) ,
            'O2'  : round(uniform(11.2, 11.7), 2)
        }
    ]

    station = randint(0, 3)

    time.sleep(1)
    client.publish(device_name[station], json.dumps(data[station]))