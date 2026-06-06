from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaConsumer
import json

app= FastAPI()

# Kafka Consumer
consumer = KafkaConsumer(
    'payment-successful',
    bootstrap_servers=['localhost:9094'],
    auto_offset_reset='earliest',  # Start from the earliest message
    enable_auto_commit=True,
    group_id='analytics-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize data from JSON
)

print("Waiting...")

def consume_payment_data():
    for message in consumer:
        payment_data = message.value
        print("Received payment data:", payment_data)
        
consume_payment_data()

# @app.get("/analytics-service")
# async def get_payment():
#     print("Listening for payment data...")
#     for message in consumer:
#         payment_data = message.value
#         return payment_data