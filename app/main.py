from fastapi import FastAPI

from app.schemas import CustomerData
from app.predict import predict_customer

from fastapi import FastAPI

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Machine Learning API for predicting customer churn using a Random Forest Pipeline.",
    version="1.0.0",
    contact={
        "name": "M.Amine bouzoffara",
        "email": "amine0nova@gmail.com"
    }
)

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API",
        "status": "Running",
    }

@app.get("/health")
def health():
    return {
        "message": "API is healthy",
        "status": "Running",
    }

@app.post("/predict")
def predict(customer: CustomerData):
    return predict_customer(customer)