from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

SAMPLE_CUSTOMER = {
    "Gender": "Female",
    "Senior_Citizen": "No",
    "Partner": "No",
    "Dependents": "No",
    "Tenure_Months": 2,
    "Phone_Service": "Yes",
    "Multiple_Lines": "No",
    "Internet_Service": "Fiber optic",
    "Online_Security": "No",
    "Online_Backup": "No",
    "Device_Protection": "No",
    "Tech_Support": "No",
    "Streaming_TV": "No",
    "Streaming_Movies": "No",
    "Contract": "Month-to-month",
    "Paperless_Billing": "Yes",
    "Payment_Method": "Electronic check",
    "Monthly_Charges": 70.7,
    "Total_Charges": 151.65,
    "CLTV": 2701,
}


def test_predict():

    response = client.post("/predict", json=SAMPLE_CUSTOMER)

    assert response.status_code == 200

    body = response.json()
    assert body["prediction"] in (0, 1)
    assert 0.0 <= body["probability"] <= 1.0
    assert body["risk_level"] in ("Low", "Medium", "High")
