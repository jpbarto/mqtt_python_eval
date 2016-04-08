import paho.mqtt.client as mqtt
from time import time
from threading import Thread, Timer

TOPIC_COUNT = 10000
PUB_PERIOD = 10

def flood_topics (client):
    for tnum in range(TOPIC_COUNT):
        client.publish ("a/b/c/{0}".format (tnum), payload = "message for topic number {0} at {1}".format (tnum, time ()))
    Timer (PUB_PERIOD, flood_topics, args = [client]).start ()

def on_connect (client, userData, flags, rc):
    print ("Connected with result code "+ str(rc))
    Thread (target = flood_topics, args = [client]).start ()

client = mqtt.Client ()
client.on_connect = on_connect

client.connect ("127.0.0.1", 1883, 60)

client.loop_forever ()
