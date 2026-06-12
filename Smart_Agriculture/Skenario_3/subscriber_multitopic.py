import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)

# Mendaftar ke topik satu per satu
client.subscribe("pertanian/greenhouse/suhu")
client.subscribe("pertanian/greenhouse/kelembaban")
client.subscribe("pertanian/greenhouse/cahaya")

print("Menerima aliran data Greenhouse...")
client.loop_forever()