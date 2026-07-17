from fastapi import FastAPI

from app.schemas import CustomerData
from app.predict import predict_customer
from app.config import API_TITLE, API_VERSION
from fastapi import FastAPI
from app.logger import logger

logger.info("Starting Customer Churn Prediction API...")
app = FastAPI(
    title=API_TITLE,
    description="Machine Learning API for predicting customer churn using a Random Forest Pipeline.",
    version=API_VERSION,
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