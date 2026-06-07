# 🛒 Retail Microservices

A scalable **E-commerce Platform** built using **Microservices Architecture**, **Apache Kafka**, **FastAPI**, **React**, and **Docker**.

This project demonstrates how modern distributed systems communicate using **event-driven architecture**, where services interact asynchronously through Kafka topics instead of direct service-to-service calls.

---

## 🚀 Features

- Microservices-based architecture
- Event-driven communication using Apache Kafka
- FastAPI backend services
- React frontend
- Kafka Producers & Consumers
- Consumer Groups
- Topic Partitioning
- Multi-Broker Kafka Cluster
- Fault Tolerance through Replication
- Kafka UI for monitoring
- Dockerized infrastructure

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │ React Frontend  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Payment Service │
                    └────────┬────────┘
                             │
                             ▼
                 Kafka Topic: payment-successful
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
       ┌─────────────────┐     ┌─────────────────┐
       │  Order Service  │     │ Analytics       │
       └────────┬────────┘     │ Service         │
                │              └─────────────────┘
                ▼
       Kafka Topic: order-successful
                │
                ▼
       ┌─────────────────┐
       │  Email Service  │
       └─────────────────┘
```

---

## 🧰 Tech Stack

### Frontend

- React
- JavaScript
- Axios

### Backend

- Python
- FastAPI
- Pydantic

### Messaging

- Apache Kafka
- Kafka UI

### Infrastructure

- Docker
- Docker Compose

---

## 📦 Microservices

### Payment Service

**Responsibilities**

- Accept payment requests
- Validate incoming payloads
- Publish payment events to Kafka

**Produces**

```text
payment-successful
```

---

### Order Service

**Responsibilities**

- Consume payment events
- Create orders
- Publish order completion events

**Consumes**

```text
payment-successful
```

**Produces**

```text
order-successful
```

---

### Analytics Service

**Responsibilities**

- Consume events from multiple Kafka topics
- Aggregate business metrics
- Track platform activity

**Consumes**

```text
payment-successful
order-successful
```

---

### Email Service

**Responsibilities**

- Send order confirmation notifications

**Consumes**

```text
order-successful
```

---

## 📨 Event Flow

### Step 1: Customer Places an Order

```json
{
  "cart": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 999.99,
      "image": "laptop.jpg"
    }
  ]
}
```

---

### Step 2: Payment Service Publishes Event

Topic:

```text
payment-successful
```

Payload:

```json
{
  "eventType": "PAYMENT_SUCCESSFUL",
  "orderId": 123,
  "amount": 999.99
}
```

---

### Step 3: Order Service Consumes Event

Creates order and publishes:

Topic:

```text
order-successful
```

Payload:

```json
{
  "eventType": "ORDER_SUCCESSFUL",
  "orderId": 123
}
```

---

### Step 4: Email Service Consumes Event

Sends order confirmation email to customer.

---

## ⚡ Kafka Concepts Demonstrated

This project implements and demonstrates:

- Kafka Producers
- Kafka Consumers
- Consumer Groups
- Topic Partitioning
- Message Serialization
- Multi-Broker Cluster
- Replication
- Leader Election
- Broker Failover
- Event-Driven Architecture
- Asynchronous Communication

---

## 🏢 Kafka Cluster Setup

Current Kafka setup:

```text
Broker 1
Broker 2
Broker 3
```

One broker acts as the Controller:

```text
Broker 1 (Controller)
Broker 2
Broker 3
```

Capabilities:

- Automatic leader election
- Replication
- Fault tolerance
- Consumer group coordination

---

## 📁 Project Structure

```text
retail-microservices/
│
├── frontend/
│   └── react-app/
│
├── services/
│   ├── payment-service/
│   ├── order-service/
│   ├── analytics-service/
│   └── email-service/
│
├── kafka/
│   └── docker-compose.yml
│
├── docs/
│
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/retail-microservices.git

cd retail-microservices
```

---

### 2. Start Kafka Cluster

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

---

### 3. Start Payment Service

```bash
cd services/payment-service

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app:app --reload --port 8001
```

---

### 4. Start Order Service

```bash
cd services/order-service

source .venv/bin/activate

uvicorn app:app --reload --port 8002
```

---

### 5. Start Analytics Service

```bash
cd services/analytics-service

source .venv/bin/activate

uvicorn app:app --reload --port 8003
```

---

### 6. Start Email Service

```bash
cd services/email-service

source .venv/bin/activate

uvicorn app:app --reload --port 8004
```

---

### 7. Start Frontend

```bash
cd frontend/react-app

npm install

npm start
```

Frontend:

```text
http://localhost:3000
```

---

## 📊 Kafka UI

Kafka UI can be accessed at:

```text
http://localhost:8080
```

Use Kafka UI to:

- View topics
- Inspect messages
- Monitor partitions
- Track consumer groups
- Observe lag and offsets

---

## 🧪 Example API Request

### Payment Service

**POST**

```http
http://localhost:8001/payment-service
```

Request Body:

```json
{
  "cart": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 999.99,
      "image": "laptop.jpg"
    }
  ]
}
```

Response:

```json
{
  "cart": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 999.99,
      "image": "laptop.jpg"
    }
  ]
}
```

---

## 🎯 Learning Objectives

This project was created to gain hands-on experience with:

- Distributed Systems
- Event-Driven Design
- Apache Kafka Internals
- FastAPI Development
- Scalable Backend Architecture
- Microservices Communication Patterns
- Fault-Tolerant Systems

---

## 🔮 Future Improvements

- PostgreSQL Integration
- Redis Caching
- Kubernetes Deployment
- API Gateway
- Service Discovery
- JWT Authentication
- Inventory Service
- Notification Service
- Elasticsearch
- Prometheus Monitoring
- Grafana Dashboards
- CI/CD Pipelines

---

## 📄 License

MIT License

Feel free to fork, modify, and use this project for learning purposes.
