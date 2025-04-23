# classifying and detecting abnormal cow behavior using accelerometer and heart rate sensor with real time alerts
Here's a detailed and well-structured `README.md` file for your GitHub repository:

---

# 🐄 Cow Behavior Monitoring System using ESP32, Accelerometer & Heart Rate Sensor

This project is an **IoT-based real-time cow behavior monitoring system** that classifies and detects abnormal behavior using data from an accelerometer (MPU6050), heart rate sensor (MAX3010x), and a temperature sensor (LM35). It sends real-time alerts via **Telegram** and visualizes data using **Blynk Cloud**.

---

## Demo Video



## 📌 Features

- 📡 **Real-time Monitoring** of cow health parameters
- 📊 **Live Data Visualization** on Blynk Cloud
- 🚨 **Instant Telegram Alerts** for abnormal conditions
- 🧠 **Behavior Classification** based on threshold logic
- 🐄 Optimized for **precision livestock farming**

---

## ⚙️ Hardware Components

| Component         | Description                     |
|------------------|---------------------------------|
| ESP32             | Main microcontroller            |
| MPU6050           | Accelerometer + Gyroscope       |
| MAX3010x          | Heart rate sensor               |
| LM35              | Temperature sensor              |
| Jumper Wires      | For connections                 |
| Breadboard        | Optional for prototyping        |
| WiFi              | Required for cloud connectivity |

---

## 🔌 Circuit Connections

| Sensor      | ESP32 Pin  |
|-------------|------------|
| MPU6050     | SDA → 21   |
|             | SCL → 22   |
| MAX3010x    | SDA → 21   |
|             | SCL → 22   |
| LM35        | OUT → 34   |
| VCC/GND     | To ESP32 3.3V & GND |

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/Prasana45/Detecting-abnormal-cow-behavior.git
```

### 2. Install Required Libraries

In Arduino IDE, install:
- `MPU6050`
- `Blynk`
- `MAX3010x`
- `HTTPClient`
- `Wire`

### 3. Edit the Code

Update the following placeholders in the code:
```cpp
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
char auth[] = "YOUR_BLYNK_TOKEN";
String BOTtoken = "YOUR_BOT_TOKEN";
String chatID = "YOUR_CHAT_ID";
```

### 4. Upload to ESP32

- Select **ESP32 Dev Module** as board
- Connect via USB
- Click **Upload**

---

## 📈 Data Monitoring

- **Blynk Cloud**: 
  - V0 = Temperature (°C)
  - V1 = Heart Rate (BPM)
  - V2 = Acceleration (m/s²)

- **Telegram**:
  - Sends alert if:
    - Temp > 39.5°C
    - Heart Rate > 100 BPM
    - Abnormal movement detected

---

## 📷 Screenshots

(Add your Blynk dashboard and Telegram alert screenshots here)

---

## ✅ Future Improvements

- Machine learning model for smart behavior classification
- GPS integration to monitor cow location
- Automated health record logging to cloud database

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✨ Acknowledgements

- [Blynk](https://blynk.io)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Arduino](https://www.arduino.cc/)

---

Let me know if you want me to generate a `LICENSE` or example dashboard layout too!
