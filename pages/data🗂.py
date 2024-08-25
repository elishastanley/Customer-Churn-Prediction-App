import streamlit as st
import pandas as pd
import pyodbc
import numpy as np
from dotenv import dotenv_values

st.set_page_config(
    page_title="Sample Data",
    page_icon="🗂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Loading environment variables from .env file
environment_variables = dotenv_values('.env')

# Retrieving credentials from the .env file
server = environment_variables.get("SERVER")
database = environment_variables.get("DATABASE")
username = environment_variables.get("USERNAME")
password = environment_variables.get("PASSWORD")

# Creating a connection string for SQL Server
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"

# Establishing a database connection using pyodbc
def get_connection():
    return pyodbc.connect(connection_string)

# Using the new st.cache_data decorator to cache the data loaded from the database
@st.cache_data
def load_data():
    with get_connection() as conn:
        return pd.read_sql_query("SELECT * FROM dbo.LP2_Telco_churn_first_3000", conn)

# Function to display the data page in Streamlit
def show_data_page():
    st.title("Data Exploration Page")

    data = load_data()  # Load data from the database
    st.write("Here is a sample of the dataset:")
    st.dataframe(data.head())  # Display the first few rows of the data

    # Allowing users to select what type of data features they want to view using a select box
    feature_type = st.selectbox(
        "Select which features to view:",
        options=('Numeric Features', 'Categorical Features'),
        index=0  # Default selection
    )

    if feature_type == 'Numeric Features':
        st.write("Showing Numeric Features:")
        numeric_data = data.select_dtypes(include=[np.number])
        st.dataframe(numeric_data.head())
    elif feature_type == 'Categorical Features':
        st.write("Showing Categorical Features:")
        categorical_data = data.select_dtypes(exclude=[np.number])
        st.dataframe(categorical_data.head())

if __name__ == "__main__":
    show_data_page()
