# IoT-Cold-Storage-Monitoring-System-AWS
# 🧊 IoT Cold Storage Monitoring System (AWS)

## 📌 Overview
This project implements a real-time IoT monitoring system to track temperature and humidity using AWS services. It simulates a cold storage environment and provides live data visualization with alert notifications.

---

## 🚀 Features
- Real-time data simulation using Python
- MQTT communication via AWS IoT Core
- Data storage using DynamoDB
- Live dashboard using Streamlit
- Email alerts using AWS SNS
- Threshold-based alert system

---

## 🏗️ Architecture

Sensor → AWS IoT Core → Rule Engine →  
→ DynamoDB (storage)  
→ SNS (alerts)  
→ Streamlit Dashboard

---

## 🛠️ Tech Stack
- Python
- AWS IoT Core
- DynamoDB
- SNS
- Streamlit
- MQTT

---

## 📂 Project Structure

iot-cold-storage-monitoring/
│
├── sensor/
│   └── sensor.py
│
├── dashboard/
│   └── app.py
│
├── certs/
│   ├── cert.pem
│   ├── private.key
│   ├── public.pem.key
│   ├── AmazonRootCA1.pem
│
├── config/
│   └── endpoint.txt
│
├── screenshots/
│   ├── dashboard.png
│   ├── dynamodb.png
│   ├── sns_email.png
│
├── requirements.txt
├── README.md



##  Install dependencies:
pip install -r requirements.txt


---

## ▶️ Run Project

Run sensor:
python sensor/sensor.py


Run dashboard:
streamlit run dashboard/app.py
---

## 🔔 Alert System

Alerts are triggered when:
temperature > 8°C


An email notification is sent using AWS SNS.

---

## 📊 Screenshots

### Dashboard
<img width="1920" height="921" alt="dashboard" src="https://github.com/user-attachments/assets/cde4ddcd-6ed1-47b9-b3b5-7869ae3a0655" />


### DynamoDB Data
<img width="1920" height="918" alt="dynamodb" src="https://github.com/user-attachments/assets/aea1e278-7be4-452c-9ed8-ebb196e7df5d" />


### SNS Email Alert
<img width="1920" height="903" alt="sns_email" src="https://github.com/user-attachments/assets/e08b26c9-1f00-47b1-b4b5-1418455d316b" />


### IoT Rule
<img width="1920" height="932" alt="iot_role" src="https://github.com/user-attachments/assets/38d13352-bd30-4f7f-8007-955d2409faae" />


---

## ⚠️ Important Notes
- AWS certificates are not included for security reasons
- Configure your own AWS IoT credentials before running

---

## 📌 Use Cases
- Cold storage monitoring
- Vaccine storage tracking
- Food supply chain monitoring

---
