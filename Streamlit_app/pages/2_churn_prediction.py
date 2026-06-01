import streamlit as st
import requests

st.title("🔮 Customer Churn Prediction")

# ------------------------
# User Inputs
# ------------------------

SeniorCitizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    value=12
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

Contract = st.selectbox(
    "Contract Type",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

InternetService = st.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Credit card",
        "Mailed check"
    ]
)

gender_Male = st.selectbox(
    "Gender",
    [0, 1]
)

Partner_Yes = st.selectbox(
    "Has Partner",
    [0, 1]
)

Dependents_Yes = st.selectbox(
    "Has Dependents",
    [0, 1]
)

# ------------------------
# Prediction Button
# ------------------------

if st.button("Predict Churn Risk"):

    customer_data = {
        "SeniorCitizen": SeniorCitizen,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "Contract": Contract,
        "InternetService": InternetService,
        "PaymentMethod": PaymentMethod,
        "gender_Male": gender_Male,
        "Partner_Yes": Partner_Yes,
        "Dependents_Yes": Dependents_Yes
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=customer_data
        )

        result = response.json()

        st.subheader("Prediction Result")

        st.success(
            f"Prediction: {result['prediction']}"
        )

        probability = result["probability"]

        st.metric(
            "Churn Probability",
            f"{probability * 100:.2f}%"
        )

        if probability >= 0.70:
            st.error("🔴 High Risk Customer")

        elif probability >= 0.40:
            st.warning("🟠 Medium Risk Customer")

        else:
            st.success("🟢 Low Risk Customer")

    except Exception as e:
        st.error(f"Error: {e}")