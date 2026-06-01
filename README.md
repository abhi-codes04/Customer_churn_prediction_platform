#  Customer Churn Analytics & Prediction Platform

## Overview

The Customer Churn Analytics & Prediction Platform is an end-to-end data analytics and machine learning project designed to analyze customer churn behavior and predict the likelihood of customer attrition.

The project combines Exploratory Data Analysis (EDA), Machine Learning, and Interactive Dashboarding to help businesses identify customers at risk of churning and support data-driven retention strategies.

---

## Business Problem

Customer churn is one of the most significant challenges faced by subscription-based businesses. Acquiring new customers is often more expensive than retaining existing ones.

This project aims to:

* Understand the factors influencing customer churn.
* Identify high-risk customer segments.
* Build predictive models for churn prediction.
* Provide an interactive dashboard for business users.

---

## Dataset

The project uses the Telco Customer Churn Dataset containing customer demographics, account information, services subscribed, and churn status.

### Dataset Features

* Customer Demographics
* Contract Type
* Internet Services
* Payment Methods
* Monthly Charges
* Total Charges
* Customer Tenure
* Churn Status

---

## Project Workflow

### 1. Data Cleaning & Preprocessing

* Handled missing values
* Converted data types
* Encoded categorical variables
* Feature scaling using StandardScaler

### 2. Exploratory Data Analysis

Performed extensive analysis to answer key business questions:

* What is the overall churn rate?
* Which contract types have the highest churn?
* How does tenure influence churn?
* How do payment methods affect retention?
* What are the major drivers of customer churn?

### 3. Machine Learning

Models evaluated:

* Logistic Regression
* Random Forest Classifier

Evaluation metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Cross Validation

### 4. Model Selection

After evaluation and comparison:

**Selected Model:** Logistic Regression

Reasons:

* Highest ROC-AUC Score
* Better Generalization
* Consistent Cross Validation Performance
* Greater Interpretability

---

## Model Performance

| Metric                   | Logistic Regression |
| ------------------------ | ------------------- |
| ROC-AUC                  | 0.862               |
| Cross Validation ROC-AUC | 0.841               |
| Cross Validation Std Dev | 0.012               |

The model demonstrated strong discriminative performance and stable behavior across multiple folds.

---

## Feature Importance Insights

Top factors influencing churn:

1. TotalCharges
2. Tenure
3. MonthlyCharges
4. Internet Service Type
5. Payment Method
6. Contract Type

Key finding:

Customer behavior and financial attributes were significantly more predictive than demographic variables.

---

## Dashboard Features

### Executive Dashboard

* Total Customers
* Churn Rate
* Average Monthly Charges
* Average Customer Tenure

### Analytics Module

* Churn Distribution Analysis
* Contract Type Analysis
* Payment Method Analysis
* Tenure Analysis

### Prediction Module

Users can:

* Enter customer information
* Predict churn probability
* View churn risk level

---

## Project Structure

```text
customer-churn-analytics-platform/
│
├── data/
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── models/
│   ├── logistic_model.pkl
│   └── scaler.pkl
│
├── streamlit_app/
│   └── app.py
│     pages/
        Analytics_Dashbaord.py
        Churn_Prediction.py
├── api/
│   └── main.py
│
├── images/
│
├── README.md
│
└── requirements.txt
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* FastAPI
* Joblib

---

## Future Improvements

* Deploy using Streamlit Cloud
* Deploy FastAPI backend
* Add SHAP Explainability
* Add Customer Segmentation
* Add Advanced Retention Recommendations
* Integrate Real-Time Prediction APIs

---

## Key Takeaways

This project demonstrates the complete machine learning lifecycle, including:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Model Training
* Model Evaluation
* Hyperparameter Tuning
* Feature Importance Analysis
* Dashboard Development
* Model Deployment Preparation

```
```
