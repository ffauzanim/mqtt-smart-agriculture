import paho.mqtt.client as mqtt
import sys

BROKER_ADDRESS = "localhost"
PORT = 1883

# Menu Pemilihan Skenario untuk Pengujian Laporan
print("=== PENGUJIAN SKENARIO SUBSCRIBER ===")
print("1. Skenario 4: Wildcard '+' (Hanya membaca Sensor dari semua sistem)")
print("2. Skenario 5: Wildcard '#' (Membaca SELURUH data Sensor & Aktuator)")
pilihan = input("Masukkan pilihan (1/2): ")

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("\n[STATUS] Dashboard Pemantauan Terhubung ke Broker!\n")
        
        if pilihan == '1':
            # [SKENARIO 4] Penggunaan Wildcard '+'
            # Memfilter data: Hanya mengambil topik yang pola level ke-3 nya adalah 'sensor'
            topik_subscribe = "pertanian/+/sensor/+"
            client.subscribe(topik_subscribe, qos=1)
            print(f"[*] Menjalankan SKENARIO 4")
            print(f"[*] Subscribed ke topik: {topik_subscribe}")
            print(f"[*] Ekspektasi: Hanya mencetak data SENSOR (Suhu, Cahaya, Soil, Amonia).\n")
            
        elif pilihan == '2':
            # [SKENARIO 5] Penggunaan Wildcard '#'
            # Menangkap seluruh pohon data di bawah 'pertanian/'
            topik_subscribe = "pertanian/#"
            client.subscribe(topik_subscribe, qos=2)
            print(f"[*] Menjalankan SKENARIO 5")
            print(f"[*] Subscribed ke topik: {topik_subscribe}")
            print(f"[*] Ekspektasi: Mencetak SEMUA data SENSOR dan status AKTUATOR.\n")
            
        else:
            print("[ERROR] Pilihan tidak valid. Keluar dari program.")
            sys.exit()
            
        print("Menunggu aliran data dari lahan...")
        print("-" * 50)
    else:
        print(f"[ERROR] Gagal terhubung, kode: {rc}")

def on_message(client, userdata, msg):
    topik = msg.topic
    payload = msg.payload.decode('utf-8')
    qos = msg.qos
    
    # Format output agar mudah dibaca pada screenshot laporan
    if "sensor" in topik:
        print(f"[\u25CF SENSOR]   Topik: {topik: <40} | QoS: {qos} | Value: {payload}")
    elif "aktuator" in topik:
        print(f"[\u25B6 AKTUATOR] Topik: {topik: <40} | QoS: {qos} | Status: {payload}")

# [SKENARIO 1] Inisialisasi Client Subscriber
client = mqtt.Client(client_id="Agro_Dashboard")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, PORT)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\n[STATUS] Menutup dashboard pemantauan...")
    client.disconnect()