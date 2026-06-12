# MQTT Smart Agriculture using Python & Mosquitto

Implementasi komunikasi MQTT menggunakan Python dan Mosquitto Broker untuk simulasi **Cyber Physical System (CPS)** pada studi kasus **Smart Agriculture**.

## Deskripsi Project

Project ini merupakan tugas praktikum implementasi MQTT yang mencakup:

* Komunikasi dasar Publisher–Subscriber
* Pengujian Quality of Service (QoS 0, 1, 2)
* Multi Topic Communication
* Wildcard Topic `+`
* Wildcard Topic `#`
* Integrasi sistem Smart Agriculture

Sistem terdiri dari 3 subsistem utama:

1. **Smart Greenhouse**

   * Sensor suhu
   * Sensor cahaya
   * Exhaust fan
   * Grow light

2. **Monitoring Lahan Terbuka**

   * Sensor soil moisture
   * Pompa air

3. **Smart Livestock Farming**

   * Sensor amonia
   * Auto feeder

---

# Struktur Folder

```bash
cps/
│
├── Smart Agriculture/
│   ├── Final/
│   │   ├── publisher.py
│   │   └── subscriber.py
│   │
│   ├── Skenario 1/
│   │   ├── publisher_basic.py
│   │   └── subscriber_basic.py
│   │
│   ├── Skenario 2/
│   │   ├── publisher_qos.py
│   │   └── subscriber_qos.py
│   │
│   ├── Skenario 3/
│   │   ├── publisher_multitopic.py
│   │   └── subscriber_multitopic.py
│   │
│   ├── Skenario 4/
│   │   ├── publisher_plus.py
│   │   └── subscriber_plus.py
│   │
│   └── Skenario 5/
│       ├── publisher_hash.py
│       └── subscriber_hash.py
│
├── report/
├── README.md
└── requirements.txt
```

---

# Requirements

Software:

* Python 3.x
* Mosquitto Broker
* Git (opsional)

Python Library:

```bash
pip install paho-mqtt
```

Atau:

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:

```txt
paho-mqtt
```

---

# Menjalankan Mosquitto Broker

Pastikan Mosquitto sudah terinstall.

Jalankan broker:

```bash
mosquitto
```

Jika berhasil:

```bash
Opening ipv4 listen socket on port 1883
```

---

# Cara Menjalankan Program

## Skenario 1 – Basic Publish Subscribe

Terminal 1:

```bash
python "Smart Agriculture/Skenario 1/subscriber_basic.py"
```

Terminal 2:

```bash
python "Smart Agriculture/Skenario 1/publisher_basic.py"
```

---

## Skenario 2 – QoS Test

Subscriber:

```bash
python "Smart Agriculture/Skenario 2/subscriber_qos.py"
```

Publisher:

```bash
python "Smart Agriculture/Skenario 2/publisher_qos.py"
```

---

## Skenario 3 – Multi Topic

Subscriber:

```bash
python "Smart Agriculture/Skenario 3/subscriber_multitopic.py"
```

Publisher:

```bash
python "Smart Agriculture/Skenario 3/publisher_multitopic.py"
```

---

## Skenario 4 – Wildcard +

Subscriber:

```bash
python "Smart Agriculture/Skenario 4/subscriber_plus.py"
```

Publisher:

```bash
python "Smart Agriculture/Skenario 4/publisher_plus.py"
```

---

## Skenario 5 – Wildcard

Subscriber:

```bash
python "Smart Agriculture/Skenario 5/subscriber_hash.py"
```

Publisher:

```bash
python "Smart Agriculture/Skenario 5/publisher_hash.py"
```

---

## Final System

Subscriber:

```bash
python "Smart Agriculture/Final/subscriber.py"
```

Publisher:

```bash
python "Smart Agriculture/Final/publisher.py"
```

---

# Teknologi yang Digunakan

* Python
* MQTT Protocol
* Mosquitto Broker
* Paho MQTT Library

---

# Author

Nama: [Isi Nama Anda]
Mata Kuliah: Cyber Physical System
Topik: Implementasi MQTT dengan Python dan Mosquitto Broker
