#! /usr/bin/env

import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("BROKER: Message received: ", str(message.payload.decode("utf-8")))

mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_port = 1883  

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "server")
client.connect(mqtt_broker)

client.loop_start()

dronesID = ["0001", "0002", "0003"]

for id in dronesID:
    client.subscribe(f"drone/position/{id}")
client.on_message = on_message

while True:
    pass  