import sqlite3
import pandas as pd


def create_connection():
    """Create a database connection."""
    conn = sqlite3.connect('predictions.db')
    return conn


def create_table():
    """Create tables for storing customer data and prediction history."""
    conn = create_connection()
    queries = [
        """
        CREATE TABLE IF NOT EXISTS customer_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gender TEXT,
            SeniorCitizen TEXT,
            Partner TEXT,
            Dependents TEXT,
            tenure INTEGER,
            PhoneService TEXT,
            MultipleLines TEXT,
            InternetService TEXT,
            OnlineSecurity TEXT,
            OnlineBackup TEXT,
            DeviceProtection TEXT,
            TechSupport TEXT,
            StreamingTV TEXT,
            StreamingMovies TEXT,
            Contract TEXT,
            PaperlessBilling TEXT,
            PaymentMethod TEXT,
            MonthlyCharges REAL,
            TotalCharges REAL,
            Prediction TEXT,
            Probability REAL,
            ModelUsed TEXT
        );
        """
    ]
    cursor = conn.cursor()
    for query in queries:
        cursor.execute(query)
    conn.commit()
    conn.close()


def save_to_customer_data(user_input):
    """Save customer data to the database."""
    conn = create_connection()
    cursor = conn.cursor()
    columns = ', '.join(user_input.keys())
    placeholders = ', '.join(['?'] * len(user_input))
    query = f"INSERT INTO customer_data ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(user_input.values()))
    conn.commit()
    conn.close()


def save_to_prediction_history(user_input, prediction, probability, model_name):
    """Save prediction data including the model used to the database."""
    conn = create_connection()
    cursor = conn.cursor()

    # Prepare data
    user_input['Prediction'] = prediction
    user_input['Probability'] = probability
    user_input['ModelUsed'] = model_name

    # Insert data
    columns = ', '.join(user_input.keys())
    placeholders = ', '.join(['?'] * len(user_input))
    query = f"INSERT INTO customer_data ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(user_input.values()))

    conn.commit()
    conn.close()



def get_prediction_history():
    """Retrieve all prediction history from the database."""
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM customer_data", conn)
    conn.close()
    return df


create_table()