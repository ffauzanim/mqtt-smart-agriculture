import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)

# Menggunakan wildcard '+' di level ke-4
client.subscribe("pertanian/greenhouse/sensor/+")

print("Subscribed ke pertanian/greenhouse/sensor/+")
client.loop_forever()