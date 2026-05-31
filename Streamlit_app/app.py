import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Churn Analytics Platform",
    layout="wide"
)

st.title("📊 Customer Churn Analytics Platform")
df = pd.read_csv('C:\CODING STUFF\Customer_churn_prediction_platform\Data\WA_Fn-UseC_-Telco-Customer-Churn.csv')
total_customers = len(df)

churn_rate = (df['Churn'] == 'Yes').mean() * 100

avg_monthly_charges = df['MonthlyCharges'].mean()

avg_tenure = df['tenure'].mean()
st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        total_customers
    )

with col2:
    st.metric(
        "Churn Rate",
        f"{churn_rate:.2f}%"
    )

with col3:
    st.metric(
        "Avg Monthly Charges",
        f"₹{avg_monthly_charges:.2f}"
    )

with col4:
    st.metric(
        "Avg Tenure",
        f"{avg_tenure:.1f} Months"
    )
    st.divider()

st.subheader("Executive Overview")

st.write("""
This dashboard provides insights into customer churn behavior,
key retention indicators, and machine learning predictions.
The objective is to identify customers at risk of churn and
support data-driven retention strategies.
""")
st.divider()

st.subheader("Customer Churn Distribution")
churn_counts = df['Churn'].value_counts()
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    data=df,
    x='Churn',
    ax=ax
)

ax.set_title(
    'Customer Churn Distribution'
)

st.pyplot(fig)
st.info(
    f"""
    The current churn rate is {churn_rate:.2f}%.
    Approximately 1 out of every 4 customers leaves the company,
    highlighting customer retention as a significant business challenge.
    """
)
st.divider()

st.subheader("Contract Type Analysis")
contract_churn = pd.crosstab(
    df['Contract'],
    df['Churn'],
    normalize='index'
) * 100

st.dataframe(
    contract_churn.round(2)
)
contract_churn_yes = (
    df.groupby('Contract')['Churn']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Churn Rate')
)

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    data=contract_churn_yes,
    x='Contract',
    y='Churn Rate',
    ax=ax
)

ax.set_title('Churn Rate by Contract Type')
ax.set_ylabel('Churn Rate (%)')

st.pyplot(fig)
st.info(
    """
    Customers with month-to-month contracts exhibit substantially higher churn rates
    than customers with one-year or two-year contracts. Longer contract commitments
    appear to improve customer retention and reduce churn risk.
    """
)
st.divider()

st.subheader("Payment Method Analysis")
payment_churn = (
    df.groupby('PaymentMethod')['Churn']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Churn Rate')
)
fig, ax = plt.subplots(figsize=(10,5))

sns.barplot(
    data=payment_churn,
    x='PaymentMethod',
    y='Churn Rate',
    ax=ax
)

ax.set_title("Churn Rate by Payment Method")
ax.set_ylabel("Churn Rate (%)")
ax.set_xlabel("Payment Method")

plt.xticks(rotation=20)

st.pyplot(fig)
highest_method = payment_churn.loc[
    payment_churn['Churn Rate'].idxmax(),
    'PaymentMethod'
]

highest_rate = payment_churn['Churn Rate'].max()

st.info(
    f"""
    {highest_method} has the highest churn rate at
    {highest_rate:.2f}%.

    Payment behavior appears to be associated with
    customer retention and should be considered
    when designing retention campaigns.
    """
)
st.divider()

st.subheader("Tenure Analysis")
fig, ax = plt.subplots(figsize=(8,5))

sns.boxplot(
    data=df,
    x='Churn',
    y='tenure',
    ax=ax
)

ax.set_title(
    'Tenure Distribution by Churn Status'
)

st.pyplot(fig)
tenure_summary = (
    df.groupby('Churn')['tenure']
      .mean()
      .reset_index()
)

st.dataframe(
    tenure_summary
)
fig, ax = plt.subplots(figsize=(6,4))

sns.barplot(
    data=tenure_summary,
    x='Churn',
    y='tenure',
    ax=ax
)

ax.set_title(
    'Average Tenure by Churn Status'
)

ax.set_ylabel(
    'Average Tenure (Months)'
)

st.pyplot(fig)
avg_churn = tenure_summary.loc[
    tenure_summary['Churn'] == 'Yes',
    'tenure'
].values[0]

avg_no_churn = tenure_summary.loc[
    tenure_summary['Churn'] == 'No',
    'tenure'
].values[0]

st.info(
    f"""
    Customers who churn have an average tenure of
    {avg_churn:.1f} months, while retained customers
    have an average tenure of {avg_no_churn:.1f} months.

    This suggests that newer customers are significantly
    more likely to leave than long-term customers,
    highlighting the importance of early retention efforts.
    """
)