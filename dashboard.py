import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_connection

def load_data():
    """Load data from the database."""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM churn_dataset", conn)
    # Convert 'Churn' from 'Yes/No' to 1/0 for analysis
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    conn.close()
    return df

def show_eda_dashboard(df):
    """Display the EDA dashboard."""
    st.title('EDA Dashboard')

    # Layout with columns for descriptive statistics and distribution selection
    col1, col2 = st.columns((1, 2))

    with col1:
        st.header('Dataset Overview')
        st.dataframe(df.describe())  # Display the descriptive statistics

    with col2:
        st.header('Select a column to view distribution')
        column_to_plot = st.selectbox('Select Column', df.columns)
        dist_fig = px.histogram(df, x=column_to_plot, color='Churn', barmode='overlay',
                                hover_data=df.columns.tolist())
        st.plotly_chart(dist_fig, use_container_width=True)

    # Additional visualizations outside the columns layout
    st.header('Monthly Charges by Churn Status')
    charges_fig = px.box(df, x='Churn', y='MonthlyCharges', notched=True, hover_data=df.columns.tolist())
    st.plotly_chart(charges_fig, use_container_width=True)

def show_analytics_dashboard(df):
    """Display the Analytics dashboard."""
    st.title('Analytics Dashboard')

    # KPIs above the visuals
    churn_rate = df['Churn'].mean() * 100
    avg_monthly_charges = df['MonthlyCharges'].mean()
    avg_tenure = df['tenure'].mean()

    st.markdown('#### Key Performance Indicators')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Churn Rate", value=f"{churn_rate:.2f}%")
    with col2:
        st.metric(label="Average Monthly Charges", value=f"${avg_monthly_charges:.2f}")
    with col3:
        st.metric(label="Average Tenure", value=f"{avg_tenure:.0f} months")

    # Visualizations below KPIs
    col1, col2 = st.columns(2)
    with col1:
        avg_tenure_churn = df.groupby('Churn')['tenure'].mean()
        churn_tenure_fig = px.bar(avg_tenure_churn, title="Average Tenure for Churned vs Non-Churned Customers")
        st.plotly_chart(churn_tenure_fig, use_container_width=True)

    with col2:
        avg_charges_churn = df.groupby('Churn')['MonthlyCharges'].mean()
        charges_metric_fig = px.bar(avg_charges_churn, title="Average Monthly Charges for Churned vs Non-Churned Customers")
        st.plotly_chart(charges_metric_fig, use_container_width=True)

def show():
    df = load_data()
    st.sidebar.header('Dashboard Type')
    dashboard_type = st.sidebar.radio("Choose Dashboard Type", ('EDA', 'Analytics'))
    
    if dashboard_type == 'EDA':
        show_eda_dashboard(df)
    elif dashboard_type == 'Analytics':
        show_analytics_dashboard(df)

if __name__ == "__main__":
    show()
