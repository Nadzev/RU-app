from paho.mqtt.client import Client
import paho.mqtt.client as paho
from paho import mqtt
import os
class Mqtt:
    def __init__(self):
        self.client = Client(client_id='', userdata=None, protocol= paho.MQTTv5)

    def on_connect(self, client, flags, rc, properties):
        print('Connected')
        
    def on_message(self, cls, topic, payload, client, qos):
        print(f'recebendo {payload}')

    def on_disconnect(self, cls, client, exc=None):
        print('Disconnected')

    def on_subscribe(self, client, mid, qos, properties):
        print(client)
        print('SUBSCRIBED')

    def ask_exit(*args):
        pass

    async def main(self):
        self.client.on_connect = self.on_connect

        print('caiuuuu')
        
        # enable TLS for secure connection
        self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        # set username and password
        self.client.username_pw_set('ruapp', 'ruapp123')
        # connect to HiveMQ Cloud on port 8883 (default for MQTT)
        self.client.connect('1585424bfe794383997ea302ee1d1e4e.s1.eu.hivemq.cloud', 8883)

        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe

        self.client.subscribe('my/teste')
        self.client.loop_forever()
        # user = os.getenv('MQTT_USER')
        # password = os.getenv('MQTT_PASSWORD')
        #host = os.getenv('MQTT_BROKER_HOST')
        #print(host)
        #self.client.connect(host)
        


