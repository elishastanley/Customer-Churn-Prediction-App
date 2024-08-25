import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

# Setting up the page
st.set_page_config(page_title="Data Dashboard", page_icon="📊",
                   layout="wide", initial_sidebar_state="expanded")

# Load data from the SQLite database
@st.cache_resource
def load_data():
    """Loading data from the SQLite database."""
    try:
        conn = sqlite3.connect('predictions.db')
        query = "SELECT * FROM Predicted_Dataset"
        df = pd.read_sql_query(query, conn)
    except sqlite3.Error as e:
        st.error(f"SQLite error: {e}")
        return pd.DataFrame()
    finally:
        conn.close()
    return df


df = load_data()

# Convert 'gender' from categorical to numeric if it exists
if 'gender' in df.columns:
    df['gender'] = df['gender'].map({'Male': 0, 'Female': 1}).fillna(-1)

numeric_df = df.select_dtypes(include=['float64', 'int64'])

st.title('Comprehensive Data Dashboard')

# Analytics Dashboard
st.header("Analytics Dashboard")
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    churn_rate = df[df['Churn'] == 'Yes'].shape[0] / \
        df.shape[0] * 100 if 'Churn' in df.columns else 0
    st.metric("Churn Rate", f"{churn_rate:.2f}%")

with kpi2:
    arpu = df['MonthlyCharges'].mean() if 'MonthlyCharges' in df.columns else 0
    st.metric("Average Revenue Per User", f"${arpu:.2f}")

with kpi3:
    average_tenure = df['tenure'].mean() if 'tenure' in df.columns else 0
    st.metric("Average Customer Tenure", f"{average_tenure:.1f} months")

# Exploratory Data Analysis Section
st.header("Exploratory Data Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Distribution of Monthly Charges")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(numeric_df['MonthlyCharges'], kde=True, color='blue', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Distribution of Tenure")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(numeric_df['tenure'], kde=True, color='green', ax=ax)
    st.pyplot(fig)

with col3:
    st.subheader("Churn Rate Pie Chart")
    churn_counts = df['Churn'].value_counts()
    fig, ax = plt.subplots(figsize=(3, 3))
    churn_counts.plot(kind='pie', labels=[
                      'Retained', 'Churned'], autopct='%1.1f%%', startangle=90, colors=['green', 'red'], ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)

new_col1, new_col2 = st.columns(2)
with new_col1:
    st.subheader("Payment Method vs Churn")
    payment_churn = pd.crosstab(df['PaymentMethod'], df['Churn'])
    fig, ax = plt.subplots(figsize=(4, 3))  
    payment_churn.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                       ha='right', fontsize=9)
    ax.set_ylabel('Counts', fontsize=10) 
    ax.set_xlabel('Payment Method', fontsize=10)
    st.pyplot(fig)

with new_col2:
    st.subheader("Contract vs Churn")
    contract_churn = pd.crosstab(df['Contract'], df['Churn'])
    fig, ax = plt.subplots(figsize=(4, 3))  
    contract_churn.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                       ha='right', fontsize=9) 
    ax.set_ylabel('Counts', fontsize=10) 
    ax.set_xlabel('Contract', fontsize=10)  
    st.pyplot(fig)
