import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("ruapp", "ruapp123")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("1585424bfe794383997ea302ee1d1e4e.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
#client.subscribe("my/teste", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("my/teste", payload="aaaaa", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()


 # enable TLS for secure connection
        # self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        # set username and password
        # self.client.username_pw_set('ruapp', 'ruapp123')
        # connect to HiveMQ Cloud on port 8883 (default for MQTT)
        # self.client.connect('1585424bfe794383997ea302ee1d1e4e.s1.eu.hivemq.cloud', 8883)

# self.client.on_message = self.on_message
# self.client.on_disconnect = self.on_disconnect
# self.client.on_subscribe = self.on_subscribe

# self.client.subscribe('ru/#',qos=1)
# # self.client.loop_forever()
# # user = os.getenv('MQTT_USER')
# # password = os.getenv('MQTT_PASSWORD')
# # host = os.getenv('MQTT_BROKER_HOST')
# host = 'localhost'
# self.client.connect(host)
# self.client.loop_start()
# print('mqtt')