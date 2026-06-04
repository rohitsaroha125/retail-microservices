from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

class PaymentRequest(BaseModel):
    id: int
    image: str
    price: float
    name: str

class CartRequest(BaseModel):
    cart: list[PaymentRequest]

@app.post("/payment-service")
async def process_payment(payment_request: CartRequest):
    return payment_request