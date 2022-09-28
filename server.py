import paho.mqtt.client as paho


def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)


def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print("TESTE" + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.connect("172.30.18.146", 1883)

client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

client.subscribe("ru/#", qos=1)

client.publish("ru/est", payload="aaaaa", qos=1)

client.loop_forever()
