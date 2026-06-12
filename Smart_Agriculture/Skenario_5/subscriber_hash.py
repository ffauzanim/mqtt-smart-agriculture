import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[Tertangkap Hash] {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)

# Menggunakan wildcard '#' di level ke-2
client.subscribe("pertanian/#")

print("Subscribed ke seluruh ekosistem pertanian/#")
client.loop_forever()