import paho.mqtt.client as mqtt
import time

# Perbaikan: Tambahkan CallbackAPIVersion.VERSION2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

client.loop_start()

# QoS 0: Fire and forget
client.publish("pertanian/lahan/suhu", "Suhu: 32 C (QoS 0)", qos=0)

# QoS 1: At least once
client.publish("pertanian/lahan/soil_moisture", "Kelembaban: 45% (QoS 1)", qos=1)

# QoS 2: Exactly once
client.publish("pertanian/lahan/pompa_air", "Status: ON (QoS 2)", qos=2)

print("Data sedang diproses untuk dikirim...")
time.sleep(2) # Jeda agar pesan QoS 2 selesai terkirim

client.loop_stop()
client.disconnect()
print("Koneksi ditutup secara aman.")