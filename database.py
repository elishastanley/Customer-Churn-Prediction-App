import sqlite3


def create_connection():
    """Create a database connection."""
    conn = sqlite3.connect('customer_churn.db')
    return conn


def create_tables():
    """Create tables in the database."""
    conn = create_connection()
    cursor = conn.cursor()

    # Create table for main data
    cursor.execute('''
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
            TotalCharges REAL
        )
    ''')

    # Create table for prediction history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prediction_history (
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
            Probability REAL
        )
    ''')

    # Create table for user credentials
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            name TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()


def add_user(email, name, password):
    """Add a user to the user_credentials table."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO user_credentials (email, name, password) VALUES (?, ?, ?)
    ''', (email, name, password))

    conn.commit()
    conn.close()


def save_to_customer_data(user_input):
    """Save customer data to the customer_data table."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO customer_data (
            gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines,
            InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
            StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
            MonthlyCharges, TotalCharges
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user_input['gender'], user_input['SeniorCitizen'], user_input['Partner'],
        user_input['Dependents'], user_input['tenure'], user_input['PhoneService'],
        user_input['MultipleLines'], user_input['InternetService'], user_input['OnlineSecurity'],
        user_input['OnlineBackup'], user_input['DeviceProtection'], user_input['TechSupport'],
        user_input['StreamingTV'], user_input['StreamingMovies'], user_input['Contract'],
        user_input['PaperlessBilling'], user_input['PaymentMethod'], user_input['MonthlyCharges'],
        user_input['TotalCharges']
    ))

    conn.commit()
    conn.close()


def save_to_prediction_history(user_input, prediction, probability):
    """Save prediction history to the prediction_history table."""
    conn = create_connection()
    cursor = conn.cursor()

    user_input['Prediction'] = 'Churn' if prediction == 1 else 'Not Churn'
    user_input['Probability'] = probability

    cursor.execute('''
        INSERT INTO prediction_history (
            gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines,
            InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
            StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
            MonthlyCharges, TotalCharges, Prediction, Probability
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user_input['gender'], user_input['SeniorCitizen'], user_input['Partner'],
        user_input['Dependents'], user_input['tenure'], user_input['PhoneService'],
        user_input['MultipleLines'], user_input['InternetService'], user_input['OnlineSecurity'],
        user_input['OnlineBackup'], user_input['DeviceProtection'], user_input['TechSupport'],
        user_input['StreamingTV'], user_input['StreamingMovies'], user_input['Contract'],
        user_input['PaperlessBilling'], user_input['PaymentMethod'], user_input['MonthlyCharges'],
        user_input['TotalCharges'], user_input['Prediction'], user_input['Probability']
    ))

    conn.commit()
    conn.close()


def verify_user(email, password):
    """Verify user credentials."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM user_credentials WHERE email = ? AND password = ?
    ''', (email, password))

    user = cursor.fetchone()
    conn.close()
    return user



create_tables()