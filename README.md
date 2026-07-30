# Customer Churn Prediction API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)

---

#  Overview

This project is an end-to-end Machine Learning application that predicts customer churn using a Random Forest classifier.

The application includes the complete ML workflow:

- Data exploration
- Data preprocessing
- Feature engineering
- Machine Learning pipeline
- REST API with FastAPI
- Docker containerization
- Automated testing
- GitHub Actions CI

The trained model is exposed through a REST API that accepts customer information and returns the churn prediction together with the probability.

---

#  Features

- End-to-End Machine Learning Pipeline
- FastAPI REST API
- Pydantic Request Validation
- Random Forest Classifier
- Docker Support
- Docker Compose
- Unit Testing with Pytest
- GitHub Actions Continuous Integration
- Logging
- Environment Configuration (.env)


---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Machine Learning | Scikit-Learn |
| API | FastAPI |
| Validation | Pydantic |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Testing | Pytest |
| Version Control | Git |
| Environment | dotenv |

---

# Project Structure

```text
customer-churn-api/

├── app/
├── training/
├── models/
├── tests/
├── data/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .github/workflows/
```

---

# Installation

```bash
git clone https://github.com/Med00amine/customer-churn-api.git

cd customer-churn-api

python -m venv .venv

source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the API

```bash
uvicorn app.main:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Docker

Build

```bash
docker build -t customer-churn-api .
```

Run

```bash
docker run -p 8000:8000 customer-churn-api
```

Docker Compose

```bash
docker compose up --build
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| POST | /predict | Predict Customer Churn |

---

# Example Request

```json
{
    "Gender":"Male",
    "Senior_Citizen":"No",
    "Partner":"Yes",
    "Dependents":"No",
    "Tenure_Months":12,
    "Phone_Service":"Yes",
    "Multiple_Lines":"No",
    "Internet_Service":"Fiber optic",
    "Online_Security":"No",
    "Online_Backup":"Yes",
    "Device_Protection":"No",
    "Tech_Support":"No",
    "Streaming_TV":"Yes",
    "Streaming_Movies":"No",
    "Contract":"Month-to-month",
    "Paperless_Billing":"Yes",
    "Payment_Method":"Electronic check",
    "Monthly_Charges":70.35,
    "Total_Charges":840.20,
    "CLTV":3500
}
```

---

# Example Response

```json
{
    "prediction":"Churn",
    "probability":81.47,
    "risk_level":"High"
}
```

---

# Machine Learning Pipeline

- Data Cleaning
- Feature Engineering
- OneHotEncoder
- StandardScaler
- ColumnTransformer
- Random Forest Classifier
- Scikit-Learn Pipeline

---

# Model Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

# Continuous Integration

Every push automatically:

- Installs dependencies
- Runs unit tests
- Verifies the project builds successfully

---

# Future Improvements

- Deploy on AWS EC2
- Add Prometheus Monitoring
- Add Grafana Dashboard
- Model Versioning with MLflow
- Authentication
- Kubernetes Deployment

---

# Author

**Mohamed Amine Bouzoffara**

