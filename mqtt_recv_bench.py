import paho.mqtt.client as mqtt
from time import time

msg_count = 0
start_ts = time ()

def on_connect (client, userData, flags, rc):
    print ("Connected with result code "+ str(rc))
    client.subscribe ("a.b.c")

def on_message (client, userData, message):
    global msg_count
    msg_count = msg_count + 1
    if msg_count % 1000 == 0:
        print "Read {0} msg in {1} sec".format (msg_count, (time () - start_ts))


client = mqtt.Client ()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set ('admin', 'admin')
client.connect ("127.0.0.1", 1883, 60)

client.loop_forever ()
