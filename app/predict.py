import joblib
import pandas as pd
from pathlib import Path


# Load model once when the API starts




# Parent directory of the current file
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models"/ "Preprocess_RandomForest_Model.pkl"

model = joblib.load(MODEL_PATH)


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

    return {
        "prediction": int(prediction),
        "prediction_label": "Churn" if prediction == 1 else "No Churn",
        "probability": round(float(probability), 4),
    }