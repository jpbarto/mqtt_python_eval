import paho.mqtt.client as mqtt
from time import time
from threading import Thread

def publish_message ():
    while True:
        client.publish ('a.b.c', payload = "hello world @ {0}".format (time ()))

def on_connect (client, userData, flags, rc):
    print ("Connected with result code "+ str(rc))
    Thread (target = publish_message).start ()

client = mqtt.Client ()
client.on_connect = on_connect

client.username_pw_set ('admin', 'admin')
client.connect ("127.0.0.1", 1883, 60)

client.loop_forever ()
