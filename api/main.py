from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
import joblib

app = FastAPI()
model = joblib.load("../models/logistic_model.pkl")
scaler = joblib.load("../models/scaler.pkl")
feature_columns = joblib.load("../models/feature_columns.pkl")
app = FastAPI()
@app.get("/")
def home():
    return {
        "message":"Customer Churn Prediction API"
    }
class CustomerData(BaseModel):
    SeniorCitizen: int
    tenure: float
    MonthlyCharges: float
    TotalCharges: float

    Contract: str
    InternetService: str
    PaymentMethod: str

    gender_Male: int = 0
    Partner_Yes: int = 0
    Dependents_Yes: int = 0
@app.post("/predict")
def predict(data: CustomerData):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )
    input_df['SeniorCitizen'] = data.SeniorCitizen
    input_df['tenure'] = data.tenure
    input_df['MonthlyCharges'] = data.MonthlyCharges
    input_df['TotalCharges'] = data.TotalCharges

    input_df['gender_Male'] = data.gender_Male
    input_df['Partner_Yes'] = data.Partner_Yes
    input_df['Dependents_Yes'] = data.Dependents_Yes
    
    if data.Contract == "One year":
        input_df['Contract_One year'] = 1

    elif data.Contract == "Two year":
        input_df['Contract_Two year'] = 1
    if data.InternetService == "Fiber optic":
        input_df['InternetService_Fiber optic'] = 1

    elif data.InternetService == "No":
        input_df['InternetService_No'] = 1
    if data.PaymentMethod == "Credit card":
        input_df[
            'PaymentMethod_Credit card (automatic)'
        ] = 1

    elif data.PaymentMethod == "Electronic check":
        input_df[
            'PaymentMethod_Electronic check'
        ] = 1

    elif data.PaymentMethod == "Mailed check":
        input_df[
            'PaymentMethod_Mailed check'
        ] = 1
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(
        scaled_input
    )[0]

    probability = model.predict_proba(
        scaled_input
    )[0][1]
    return {
        "prediction":
            "Churn" if prediction else "No Churn",

        "probability":
            round(float(probability),4)
    }
@app.post("/predict")
def predict(data: CustomerData):

    return {
        "status":"working"
    }