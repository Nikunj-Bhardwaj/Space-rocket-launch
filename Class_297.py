from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
#Set the Hostname, Port & TopicName




client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client
#Define the first page of the web application

#Define the button page of the web application

#Define the Release Orbital Arm button and connect with MQTT server

#Define the Main Engine Test button and connect with MQTT server

#Define the Activate Hydrogen button and connect with MQTT server

#Define the Main Engine Ignite button and connect with MQTT server

#Define the Hydrogen Vent Arm button and connect with MQTT server

#Define the Ignite both SRB's button and connect with MQTT server

if __name__ == "__main__":
    app.run(port=5001)





