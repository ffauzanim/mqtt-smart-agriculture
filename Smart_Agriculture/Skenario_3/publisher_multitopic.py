import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client()
client.connect("localhost", 1883)

try:
    while True:
        temp = random.randint(25, 35)
        hum = random.randint(60, 90)
        light = random.randint(100, 500)

        client.publish("pertanian/greenhouse/suhu", str(temp))
        client.publish("pertanian/greenhouse/kelembaban", str(hum))
        client.publish("pertanian/greenhouse/cahaya", str(light))

        print(f"Data dikirim -> Suhu: {temp}C | Kelembaban: {hum}% | Cahaya: {light} Lux")
        time.sleep(3)
except KeyboardInterrupt:
    client.disconnect()