import paho.mqtt.client as mqtt

def on_connect (client, userData, flags, rc):
    print ("Connected with result code "+ str(rc))
    client.publish ('tfl/road/a24/request/bob', payload = "hello world")

client = mqtt.Client ()
client.on_connect = on_connect

client.username_pw_set ('admin', 'admin')
client.connect ("127.0.0.1", 1883, 60)

client.loop_forever ()
