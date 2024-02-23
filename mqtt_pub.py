#! /usr/bin/env

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time, datetime
import json


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(mqttBroker)

dronesID = [
    1253416,
    132156,
    121336,
    1484663,
    3659688,
    9887,
    889899,
]



while True:
    for drone in dronesID:
        position = {
        "drone_id" : drone, 
        "lat" : uniform(34.0000000, 36.0000000),
        "long" : uniform(3.0000000, 4.0000000),
        "time" : str(datetime.datetime.now())
        }
        client.publish(f"drone/{position['drone_id']}/POSITION", json.dumps(position))
        print("Just published " + json.dumps(position) + " to Topic POSITION")
        time.sleep(1)