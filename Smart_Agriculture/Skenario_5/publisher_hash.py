import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883)

client.publish("pertanian/greenhouse/sensor/suhu", "28 C")
client.publish("pertanian/lahan/sensor/soil_moisture", "50%")
client.publish("pertanian/peternakan/aktuator/feeder", "DISPENSING")

print("Data dari 3 sistem berbeda dikirim.")
client.disconnect()