from fastapi import FastAPI
from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    'order-successful',
    bootstrap_servers=['localhost:9094', 'localhost:9095', 'localhost:9096'],
    auto_offset_reset='earliest',  # Start from the earliest message
    enable_auto_commit=True,
    group_id='email-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize data from JSON
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9094', 'localhost:9095', 'localhost:9096'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize data to JSON
)

def consume_order_data():
    try:
        for message in consumer:
            order_data = message.value
            print("Received order data:", order_data)
            email_data = {'name': order_data['name']}
            producer.send('email-successful', email_data)
            # Here you can implement the logic to send an email using the order data
    except Exception as e:
        print("Error consuming order data:", e)

consume_order_data()