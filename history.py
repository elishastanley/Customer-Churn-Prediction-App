import streamlit as st
import pandas as pd
from database import get_connection

def fetch_history():
    """Fetch all prediction history from the database."""
    conn = get_connection()
    query = """
        SELECT * FROM customer_data
        ORDER BY id DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def show():
    st.title('Prediction History')

    df = fetch_history()

    # Filters for the data
    st.sidebar.header('Filters')
    model_used = st.sidebar.multiselect('Model Used', options=df['ModelUsed'].unique())
    prediction_result = st.sidebar.multiselect('Prediction', options=df['Prediction'].unique())

    if model_used:
        df = df[df['ModelUsed'].isin(model_used)]
    if prediction_result:
        df = df[df['Prediction'].isin(prediction_result)]

    st.header('Prediction Results')
    st.dataframe(df)

if __name__ == "__main__":
    show()
