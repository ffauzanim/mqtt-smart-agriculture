import paho.mqtt.client as mqtt
import time
import random

# Konfigurasi Broker
BROKER_ADDRESS = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("[STATUS] Publisher Utama Terhubung ke Mosquitto Broker!")
    else:
        print(f"[ERROR] Gagal terhubung, kode: {rc}")

# [SKENARIO 1] Inisialisasi Client Publisher untuk komunikasi dasar
client = mqtt.Client(client_id="Agro_Publisher_Master")
client.on_connect = on_connect
client.connect(BROKER_ADDRESS, PORT)
client.loop_start()

try:
    while True:
        print("\n" + "="*50)
        print("MENGIRIM DATA DARI 3 SISTEM PERTANIAN PINTAR")
        print("="*50)

        # ---------------------------------------------------------
        # SISTEM 1: SMART GREENHOUSE
        # ---------------------------------------------------------
        suhu_gh = round(random.uniform(28.0, 35.0), 1)
        status_fan = "ON" if suhu_gh > 32.0 else "OFF"
        
        cahaya_lux = random.randint(100, 1000)
        status_lampu = "ON" if cahaya_lux < 400 else "OFF"
        
        # [SKENARIO 3] Menggunakan beberapa topik yang berbeda
        # [SKENARIO 2] Variasi QoS 0 (Sensor yang perubahannya kontinu & tidak fatal jika hilang)
        client.publish("pertanian/greenhouse/sensor/suhu", suhu_gh, qos=0)
        client.publish("pertanian/greenhouse/sensor/cahaya", cahaya_lux, qos=0)
        
        # [SKENARIO 2] Variasi QoS 2 (Aktuator fisik yang tidak boleh double-trigger/flicker)
        client.publish("pertanian/greenhouse/aktuator/exhaust_fan", status_fan, qos=2)
        client.publish("pertanian/greenhouse/aktuator/lampu", status_lampu, qos=2)
        
        print(f"[Greenhouse] Suhu: {suhu_gh}°C | Cahaya: {cahaya_lux} Lux")
        print(f"             Fan: {status_fan}   | Lampu UV: {status_lampu}")

        # ---------------------------------------------------------
        # SISTEM 2: MONITORING LAHAN TERBUKA
        # ---------------------------------------------------------
        soil_moisture = random.randint(20, 80)
        status_pompa = "ON" if soil_moisture < 40 else "OFF"
        
        # [SKENARIO 2] Variasi QoS 1 (Sensor krusial, minimal harus sampai 1 kali)
        client.publish("pertanian/lahan/sensor/soil_moisture", soil_moisture, qos=1)
        client.publish("pertanian/lahan/aktuator/pompa_air", status_pompa, qos=2)
        print(f"[Lahan]      Soil Moisture: {soil_moisture}% | Pompa Air: {status_pompa}")

        # ---------------------------------------------------------
        # SISTEM 3: SMART LIVESTOCK (PETERNAKAN)
        # ---------------------------------------------------------
        gas_amonia = round(random.uniform(10.0, 30.0), 1)
        status_pakan = random.choice(["STANDBY", "DISPENSING"])
        
        client.publish("pertanian/peternakan/sensor/amonia", gas_amonia, qos=1)
        client.publish("pertanian/peternakan/aktuator/auto_feeder", status_pakan, qos=2)
        print(f"[Peternakan] Gas Amonia: {gas_amonia}ppm | Auto Feeder: {status_pakan}")

        time.sleep(5) # Jeda pengiriman 5 detik

except KeyboardInterrupt:
    print("\n[STATUS] Mematikan sistem publisher...")
    client.loop_stop()
    client.disconnect()