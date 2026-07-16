from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    Gender: str = Field(default="gender")
    Senior_Citizen: str = Field(default="senior_citizen")
    Partner: str = Field(default="partner")
    Dependents: str = Field(default="dependents")
    Tenure_Months: int = Field(default=0)
    Phone_Service: str = Field(default="phone_service ")
    Multiple_Lines: str = Field(default="multiple_lines")
    Internet_Service: str = Field(default="internet_service")
    Online_Security: str = Field(default="online_security")
    Online_Backup: str = Field(default="online_backup")
    Device_Protection: str = Field(default="device_protection")
    Tech_Support: str = Field(default="tech_support")
    Streaming_TV: str = Field(default="streaming_tv")
    Streaming_Movies: str = Field(default="streaming_movies")
    Contract: str = Field(default="contract")
    Paperless_Billing: str = Field(default="paperless_billing")
    Payment_Method: str = Field(default="payment_method")
    Monthly_Charges: float = Field(default=0.0)
    Total_Charges: float = Field(default=0.0)
    CLTV: int = Field(default=0)