import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883)

client.publish("pertanian/greenhouse/sensor/suhu", "30 C")
client.publish("pertanian/greenhouse/sensor/cahaya", "450 Lux")
client.publish("pertanian/greenhouse/aktuator/lampu", "ON") # Beda direktori level 3

print("Data sensor dan aktuator greenhouse dikirim.")
client.disconnect()