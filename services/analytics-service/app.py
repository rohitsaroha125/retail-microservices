from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaConsumer
import json

app= FastAPI()

# Kafka Consumer
consumer = KafkaConsumer(
    'payment-successful',
    'order-successful',
    'email-successful',
    bootstrap_servers=['localhost:9094'],
    auto_offset_reset='earliest',  # Start from the earliest message
    enable_auto_commit=True,
    group_id='analytics-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize data from JSON
)

print("Waiting...")

def consume_payment_data():
    for message in consumer:
        match message.topic:
            case 'payment-successful':
                handle_payment_data(message.value)
            case 'order-successful':
                handle_order_data(message.value)
            case 'email-successful':
                handle_email_data(message.value)

def handle_payment_data(payment_data):
    print("Received payment data:", payment_data)
    # Here you can implement the logic to analyze payment data

def handle_order_data(order_data):
    print("Received order data:", order_data)
    # Here you can implement the logic to analyze order data

def handle_email_data(email_data):
    print("Received email data:", email_data)
    # Here you can implement the logic to analyze email data
        
consume_payment_data()

# @app.get("/analytics-service")
# async def get_payment():
#     print("Listening for payment data...")
#     for message in consumer:
#         payment_data = message.value
#         return payment_data