import streamlit as st

st.set_page_config(
    page_title="Customer Churn Analytics Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Analytics & Prediction Platform")

st.markdown("---")

st.header("Project Overview")

st.write("""
This platform helps businesses analyze customer churn behavior
and predict customer attrition using Machine Learning.

The project combines Exploratory Data Analysis (EDA),
Machine Learning, FastAPI, and Streamlit to support
data-driven retention strategies.
""")

st.markdown("---")

st.header("Key Features")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Analytics Dashboard")

    st.write("""
    - Executive KPIs
    - Churn Distribution Analysis
    - Contract Type Analysis
    - Payment Method Analysis
    - Tenure Analysis
    """)

with col2:
    st.subheader("🔮 Prediction System")

    st.write("""
    - Real-Time Churn Prediction
    - Logistic Regression Model
    - Churn Probability Scoring
    - Risk Classification
    - FastAPI Backend Integration
    """)

st.markdown("---")

st.header("Machine Learning Pipeline")

st.write("""
1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis
3. Feature Engineering
4. Model Training
5. Cross Validation
6. Hyperparameter Tuning
7. Model Deployment using FastAPI
8. Interactive Visualization using Streamlit
""")

st.markdown("---")

st.header("Model Performance")

st.metric(
    label="ROC-AUC Score",
    value="0.862"
)

st.metric(
    label="Cross Validation ROC-AUC",
    value="0.841"
)

st.markdown("---")

st.success(
    "Use the sidebar to explore the Analytics Dashboard and Churn Prediction modules."
)