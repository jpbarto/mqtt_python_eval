import paho.mqtt.client as mqtt

def on_connect (client, userData, flags, rc):
    print ("Connected with result code "+ str(rc))
    client.publish ('a/b/c', payload = "hello world")

client = mqtt.Client ()
client.on_connect = on_connect

client.connect ("127.0.0.1", 1883, 60)

client.loop_forever ()
