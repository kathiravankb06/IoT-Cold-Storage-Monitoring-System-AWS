import json
import time
import random
from awscrt import mqtt
from awsiot import mqtt_connection_builder

ENDPOINT = "a2lprd7eqbu24f-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "testDevice"
TOPIC = "coldroom/data"

PATH_TO_CERT = r"C:\Users\kathi\Downloads\iot_project\cert.pem"
PATH_TO_KEY = r"C:\Users\kathi\Downloads\iot_project\private.key"
PATH_TO_ROOT = r"C:\Users\kathi\Downloads\iot_project\AmazonRootCA1.pem"

mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERT,
    pri_key_filepath=PATH_TO_KEY,
    client_id=CLIENT_ID,
    ca_filepath=PATH_TO_ROOT,
)

mqtt_connection.connect().result()

print("Connected to AWS IoT")

mode = input("Enter mode (low / high / random): ").strip().lower()

while True:

    if mode == "low":
        temperature = random.randint(4, 7)   # ❌ should NOT trigger SNS
    elif mode == "high":
        temperature = random.randint(10, 15) # ✅ should trigger SNS
    else:
        temperature = random.randint(5, 15)  # mixed

    payload = {
        "id": str(int(time.time())),  # better unique ID
        "temperature": temperature,
        "humidity": random.randint(60, 90),
        "time": time.time()
    }

    mqtt_connection.publish(
        topic=TOPIC,
        payload=json.dumps(payload),
        qos=mqtt.QoS.AT_LEAST_ONCE
    )

    print("Sent:", payload)
    time.sleep(5)