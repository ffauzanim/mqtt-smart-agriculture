# Praktikum CPS - Skenario 1: Komunikasi Dasar
# Oleh: Faaza Fauzan Adzim (245150307111010)

import paho.mqtt.client as mqtt

broker = "localhost"
topic = "pertanian/greenhouse/suhu"

client = mqtt.Client()
client.connect(broker, 1883)

client.publish(topic, "Suhu = 30 C")
print("Data sensor suhu terkirim ke broker")

client.disconnect()