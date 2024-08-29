import pandas as pd
import random
from faker import Faker

fake = Faker()

# Possible choices for categorical fields
choices = {
    'gender': ['Male', 'Female'],
    'SeniorCitizen': ['Yes', 'No'],
    'Partner': ['Yes', 'No'],
    'Dependents': ['Yes', 'No'],
    'PhoneService': ['Yes', 'No'],
    'MultipleLines': ['Yes', 'No', 'No phone service'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['Yes', 'No', 'No internet service'],
    'OnlineBackup': ['Yes', 'No', 'No internet service'],
    'DeviceProtection': ['Yes', 'No', 'No internet service'],
    'TechSupport': ['Yes', 'No', 'No internet service'],
    'StreamingTV': ['Yes', 'No', 'No internet service'],
    'StreamingMovies': ['Yes', 'No', 'No internet service'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['Yes', 'No'],
    'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
}

# Generating dummy data
data = {
    'gender': [random.choice(choices['gender']) for _ in range(100)],
    'SeniorCitizen': [random.choice(choices['SeniorCitizen']) for _ in range(100)],
    'Partner': [random.choice(choices['Partner']) for _ in range(100)],
    'Dependents': [random.choice(choices['Dependents']) for _ in range(100)],
    'tenure': [random.randint(1, 72) for _ in range(100)],  # Tenure could be 1 to 72 months
    'PhoneService': [random.choice(choices['PhoneService']) for _ in range(100)],
    'MultipleLines': [random.choice(choices['MultipleLines']) for _ in range(100)],
    'InternetService': [random.choice(choices['InternetService']) for _ in range(100)],
    'OnlineSecurity': [random.choice(choices['OnlineSecurity']) for _ in range(100)],
    'OnlineBackup': [random.choice(choices['OnlineBackup']) for _ in range(100)],
    'DeviceProtection': [random.choice(choices['DeviceProtection']) for _ in range(100)],
    'TechSupport': [random.choice(choices['TechSupport']) for _ in range(100)],
    'StreamingTV': [random.choice(choices['StreamingTV']) for _ in range(100)],
    'StreamingMovies': [random.choice(choices['StreamingMovies']) for _ in range(100)],
    'Contract': [random.choice(choices['Contract']) for _ in range(100)],
    'PaperlessBilling': [random.choice(choices['PaperlessBilling']) for _ in range(100)],
    'PaymentMethod': [random.choice(choices['PaymentMethod']) for _ in range(100)],
    'MonthlyCharges': [round(random.uniform(29.99, 130.00), 2) for _ in range(100)],  # Random monthly charges
    'TotalCharges': [round(random.uniform(100.0, 8000.0), 2) for _ in range(100)]  # Random total charges
}

df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('dummy_data.csv', index=False)
