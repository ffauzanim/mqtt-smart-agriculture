import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic} | QoS: {msg.qos} | Message: {msg.payload.decode()}")

# Perbaikan: Tambahkan CallbackAPIVersion.VERSION2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect("localhost", 1883)

client.subscribe("pertanian/lahan/suhu", qos=2)
client.subscribe("pertanian/lahan/soil_moisture", qos=2)
client.subscribe("pertanian/lahan/pompa_air", qos=2)

print("Menunggu data untuk analisis QoS...")
client.loop_forever()