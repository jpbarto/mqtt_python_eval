import paho.mqtt.client as mqtt

def on_connect (client, userData, flags, rc):
    print ("Connected with result code "+ str(rc))
    client.subscribe ("qos/ev/al", qos = 2)

def on_message (client, userData, message):
    print (message.topic +": "+ str(message.payload))

client = mqtt.Client (client_id = 'paho_qos_eval_003', clean_session = False)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set ('admin', 'admin')
client.connect ("127.0.0.1", 1883, 60)

client.loop_forever ()
