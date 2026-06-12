import paho.mqtt.client as mqtt

broker = "localhost"
topic = "pertanian/greenhouse/suhu"

def on_message(client, userdata, msg):
    print(f"Topik: {msg.topic}")
    print(f"Pesan: {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, 1883)
client.subscribe(topic)

print("Menunggu data dari sensor...")
client.loop_forever()