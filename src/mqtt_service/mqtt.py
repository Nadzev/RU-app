from paho.mqtt.client import Client
import paho.mqtt.client as paho
from src.mqtt_service.message_handler import MessageHandler
import os

class Mqtt:
    def __init__(self,client_id):
        self.client = Client(client_id=client_id)
        # self.client = Client(client_id='', userdata=None, protocol= paho.MQTTv5)

    def on_connect(self, client, userdata, flags, rc, properties=None):
        self.client.subscribe('ru/est',qos=1)
        print('Connected')
        
    def on_message(self, cls, topic, payload):
        MessageHandler.execute_query(payload.payload)
        print(f'recebendo {payload.payload}')

    def on_disconnect(self, cls, client, exc=None):
        print('Disconnected')

    def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
        print(client)
        print('SUBSCRIBED')

    def ask_exit(*args):
        pass

    def main(self):
        self.client.on_connect = self.on_connect        

        self.client.on_message =  self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe

        self.client.subscribe('ru/#',qos=1)
        host = '172.25.83.153'
        # host = 'localhost'
        self.client.connect(host)
        self.client.loop_start()
        # self.client.loop_forever()
        print('mqtt')


