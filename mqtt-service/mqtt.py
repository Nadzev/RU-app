from paho.mqtt.client import Client
import os
class Mqtt:
    def __init__(self):
        self.client = Client('ru-app')
    
    def on_connect(self, client, flags, rc, properties):
        print('Connected')
        client.subscribe('topico_teste')
        
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
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe
        # user = os.getenv('MQTT_USER')
        # password = os.getenv('MQTT_PASSWORD')
        host = os.getenv('MQTT_BROKER_HOST')
        print(host)
        self.client.connect(host)
        


