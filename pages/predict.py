import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Theme of the app
st.set_page_config(
    page_title="Churn Prediction App",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Loading your model and preprocessing tools
with open('Models/churn_model_components.pkl', 'rb') as file:
    components = pickle.load(file)

preprocessor = components['preprocessing']['preprocessor']
models = components['tuned_models']

def predict(attributes):
    df = pd.DataFrame([attributes], columns=[
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
        'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
    ])
    processed_df = preprocessor.transform(df)
    pred = models['random_forest'].predict(processed_df)
    prob = models['random_forest'].predict_proba(processed_df)
    return pred[0], np.max(prob)

st.title('Customer Churn Prediction Tool')
st.markdown("### Please input the required fields to predict customer churn")


cols1 = st.columns(3)
cols2 = st.columns(3)
cols3 = st.columns(3)

with cols1[0]:
    st.header("Personal Details")
    gender = st.selectbox('Gender', ['Male', 'Female'])
    senior_citizen = st.selectbox('Senior Citizen', ['Yes', 'No'])
    partner = st.selectbox('Partner', ['Yes', 'No'])

with cols1[1]:
    st.header("Subscription Details")
    contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
    payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

with cols1[2]:
    st.header("Service Options")
    phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
    multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])

with cols2[0]:
    st.header("Internet & Security")
    internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])

with cols2[1]:
    st.header("Backup & Protection")
    online_backup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])

with cols2[2]:
    st.header("Support & Streaming")
    tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])

with cols3[0]:
    streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
    dependents = st.selectbox('Dependents', ['Yes', 'No'])

with cols3[1]:
    st.header("Charges & Tenure")
    monthly_charges = st.slider('Monthly Charges', min_value=0.0, max_value=200.0, value=70.0, step=0.5)
    total_charges = st.slider('Total Charges', min_value=0.0, max_value=10000.0, value=150.0, step=0.5)

with cols3[2]:
    tenure = st.number_input('Tenure (in months)', min_value=0, max_value=100, value=1)


user_input = {
    'gender': gender, 'SeniorCitizen': 'Yes' if senior_citizen == 'Yes' else 'No', 'Partner': partner, 'Dependents': dependents,
    'tenure': tenure, 'PhoneService': phone_service, 'MultipleLines': multiple_lines,
    'InternetService': internet_service, 'OnlineSecurity': online_security, 'OnlineBackup': online_backup,
    'DeviceProtection': device_protection, 'TechSupport': tech_support, 'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies, 'Contract': contract, 'PaperlessBilling': paperless_billing,
    'PaymentMethod': payment_method, 'MonthlyCharges': monthly_charges, 'TotalCharges': total_charges
}

# Prediction 
if st.button('Predict Churn'):
    prediction, probability = predict(user_input)
    st.success(f'Prediction: {"Churn" if prediction == 1 else "No Churn"} with Probability: {probability:.2f}')


