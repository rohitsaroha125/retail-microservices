from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from kafka import KafkaProducer
import json

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9094', 'localhost:9095', 'localhost:9096'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize data to JSON
)


class PaymentRequest(BaseModel):
    id: int
    image: str
    price: float
    name: str

class CartRequest(BaseModel):
    cart: list[PaymentRequest]

@app.post("/payment-service")
async def process_payment(payment_request: CartRequest):
    try:
        producer.send('payment-successful', payment_request.dict())
    except Exception as e:
        print("Error processing payment:", e)
    return payment_request