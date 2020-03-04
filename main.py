import paho.mqtt.client as mqtt


# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
    mqttc.publish("/data", "my message")

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client("client-socks",transport='websockets')
# Assign event callbacks
mqttc.connect("mqtt.eclipse.org",80)
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.publish('/data', "my message")
