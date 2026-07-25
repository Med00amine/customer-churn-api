import joblib
import pandas as pd
from app.logger import logger
from app.config import MODEL_PATH
from dotenv import load_dotenv
import os
# Load model once when the API starts




load_dotenv()
logger.info("Loading trained model...")
MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pkl")
logger.info("Model loaded successfully.")

# Mapping from API field names -> training column names


COLUMN_MAPPING = {
    "Senior_Citizen": "Senior Citizen",
    "Tenure_Months": "Tenure Months",
    "Phone_Service": "Phone Service",
    "Multiple_Lines": "Multiple Lines",
    "Internet_Service": "Internet Service",
    "Online_Security": "Online Security",
    "Online_Backup": "Online Backup",
    "Device_Protection": "Device Protection",
    "Tech_Support": "Tech Support",
    "Streaming_TV": "Streaming TV",
    "Streaming_Movies": "Streaming Movies",
    "Paperless_Billing": "Paperless Billing",
    "Payment_Method": "Payment Method",
    "Monthly_Charges": "Monthly Charges",
    "Total_Charges": "Total Charges",
}

logger.info("Received prediction request.")
try:
    logger.info("Starting prediction...")
    def predict_customer(customer):
        """
        Predict customer churn.

        Parameters
        ----------
        customer : CustomerData
            Validated Pydantic object.

        Returns
        -------
        dict
            Prediction and probability.
        """

        # Convert Pydantic model to dictionary
        customer_dict = customer.model_dump()

        # Convert dictionary to DataFrame
        df = pd.DataFrame([customer_dict])

        # Rename columns to match training data
        df.rename(columns=COLUMN_MAPPING, inplace=True)

        # Predict
        prediction = model.predict(df)[0]

        probability = model.predict_proba(df)[0][1]
        logger.info(f"Prediction={prediction} Probability={probability:.4f}")
        risk_level = "High" if probability > 0.7 else "Medium" if probability > 0.4 else "Low"
        if risk_level == "High":
            recommendation = "Offer a retention discount and contact the customer."
        elif risk_level == "Medium":
            recommendation = "Send a personalized promotion."
        else:
            recommendation = "No action required."
        
        logger.info("Prediction completed successfully.")
        return {
            "prediction": int(prediction),
            "prediction_label": "Churn" if prediction == 1 else "No Churn",
            "probability": round(float(probability), 4),
            "risk_level": risk_level,
            "recommendation": recommendation
        }

except Exception as e:
    logger.error(f"Error during prediction: {e}")
    raise e