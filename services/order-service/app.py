from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaConsumer
import json

app= FastAPI()

