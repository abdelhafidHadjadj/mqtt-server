#! usr/bin/env
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client( mqtt.CallbackAPIVersion.VERSION1,"go_app")
client.connect(mqttBroker)

client.loop_start()

dronesID = [
    56421,
    132156,
    544648,
    99563,
    3659688,
    9887,
    889899,
]

for id in dronesID:
    client.subscribe(f"drone/{id}/POSITION")
    client.on_message = on_message
time.sleep(30)
client.loop_end()