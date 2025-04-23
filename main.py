#include <WiFi.h>
#include <Wire.h>
#include <HTTPClient.h>
#include <MPU6050.h>
#include <BlynkSimpleEsp32.h>
#include "MAX3010x.h"  // Library for MAX3010x

// WiFi credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Blynk auth token
char auth[] = "YOUR_BLYNK_TOKEN";

// Telegram Bot
String BOTtoken = "YOUR_BOT_TOKEN";
String chatID = "YOUR_CHAT_ID";

// MPU6050
MPU6050 mpu;
float accel_threshold = 1.5;  // Adjust as needed

// Temperature (LM35 connected to A0)
#define TEMP_PIN 34  // analog pin

// Heart Rate
MAX3010x pulseSensor;
int heartRate = 0;

// Thresholds
float temp_threshold = 39.5;
int heart_threshold = 100;

void sendTelegram(String message) {
  HTTPClient http;
  String url = "https://api.telegram.org/bot" + BOTtoken + "/sendMessage?chat_id=" + chatID + "&text=" + message;
  http.begin(url);
  http.GET();
  http.end();
}

float readTemperature() {
  int raw = analogRead(TEMP_PIN);
  float voltage = raw * 3.3 / 4095.0;
  float tempC = voltage * 100;  // LM35: 10mV = 1°C
  return tempC;
}

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // MPU6050
  mpu.initialize();

  // MAX3010x init
  if (!pulseSensor.begin(Wire)) {
    Serial.println("MAX3010x not found. Check wiring!");
    while (1);
  }

  // WiFi + Blynk
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Blynk.begin(auth, ssid, password);
  Serial.println("Connected!");
}

void loop() {
  Blynk.run();

  // Read MPU6050
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);
  float accel = sqrt(ax * ax + ay * ay + az * az) / 16384.0;

  // Read temperature
  float temp = readTemperature();

  // Read heart rate from MAX3010x
  pulseSensor.check();  // Updates internal data
  heartRate = pulseSensor.getHeartRate();

  // Send data to Blynk
  Blynk.virtualWrite(V0, temp);
  Blynk.virtualWrite(V1, heartRate);
  Blynk.virtualWrite(V2, accel);

  // Trigger Telegram alert if abnormal
  if (temp > temp_threshold || heartRate > heart_threshold || accel > accel_threshold) {
    String alert = "⚠ Cow Behavior Alert:\n";
    if (temp > temp_threshold) alert += "• High Temp: " + String(temp) + "°C\n";
    if (heartRate > heart_threshold) alert += "• High HR: " + String(heartRate) + " bpm\n";
    if (accel > accel_threshold) alert += "• Sudden Movement Detected\n";
    sendTelegram(alert);
  }

  delay(5000);  // Check every 5 seconds
}
