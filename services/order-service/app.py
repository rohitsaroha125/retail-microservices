from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaConsumer, KafkaProducer
import json

app= FastAPI()

producer = KafkaProducer(
    bootstrap_servers=['localhost:9094', 'localhost:9095', 'localhost:9096'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')  # Serialize data to JSON
)

# Kafka Consumer
consumer = KafkaConsumer(
    'payment-successful',
    bootstrap_servers=['localhost:9094', 'localhost:9095', 'localhost:9096'],
    auto_offset_reset='earliest',  # Start from the earliest message
    enable_auto_commit=True,
    group_id='order-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize data from JSON
)

print("Waiting...")

def consume_payment_data():
    for message in consumer:
        try:
            payment_data = message.value
            print("Received payment:", payment_data['cart'])
            order_data = {'name': payment_data['cart'][0]['name'], 'price': payment_data['cart'][0]['price']}  # Extract relevant order data
            print("Extracted order data:", order_data)
            producer.send('order-successful', order_data)  # Send data to 'order-successful' topic
            print("Sent order data to 'order-successful' topic:", order_data)
        except Exception as e:
            print("Error processing payment data:", e)

consume_payment_data()