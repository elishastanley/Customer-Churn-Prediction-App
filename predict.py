import streamlit as st
import pandas as pd
import joblib
from database import get_connection

# Load models and preprocessing pipeline
model_path = 'Models/churn_model_components.pkl'
loaded_components = joblib.load(model_path)
preprocessor = loaded_components['preprocessing']['preprocessor']
tuned_models = loaded_components['tuned_models']

def predict_single(customer_data):
    # Process the input data through the preprocessor
    processed_data = preprocessor.transform(pd.DataFrame([customer_data]))
    # Predict using the loaded models
    predictions = {name: model.predict_proba(processed_data)[:, 1][0] for name, model in tuned_models.items()}
    return predictions

def save_prediction(data, predictions):
    conn = get_connection()
    cursor = conn.cursor()
    # Save each prediction with model details to the database
    for model, probability in predictions.items():
        cursor.execute("""
            INSERT INTO customer_data (gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService,
                                       MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection,
                                       TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling,
                                       PaymentMethod, MonthlyCharges, TotalCharges, Prediction, Probability, ModelUsed)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (*data.values(), 'Yes' if probability > 0.5 else 'No', probability, model))
    conn.commit()
    conn.close()

def show():
    st.title('Customer Churn Prediction')
    
    with st.form("prediction_form"):
        # Using expanders to categorize form inputs
        with st.expander("Basic Information"):
            col1, col2 = st.columns(2)
            with col1:
                gender = st.selectbox('Gender', ['Male', 'Female'])
                SeniorCitizen = st.selectbox('Senior Citizen', ['Yes', 'No'])
                Partner = st.selectbox('Partner', ['Yes', 'No'])
                Dependents = st.selectbox('Dependents', ['Yes', 'No'])
            with col2:
                tenure = st.number_input('Tenure', min_value=0)
                PhoneService = st.selectbox('Phone Service', ['Yes', 'No'])
                MultipleLines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
        
        with st.expander("Service Details"):
            col1, col2 = st.columns(2)
            with col1:
                InternetService = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
                OnlineSecurity = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
                OnlineBackup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
            with col2:
                DeviceProtection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
                TechSupport = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
                StreamingTV = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
                StreamingMovies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])

        with st.expander("Account Information"):
            Contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
            PaperlessBilling = st.selectbox('Paperless Billing', ['Yes', 'No'])
            PaymentMethod = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
            MonthlyCharges = st.number_input('Monthly Charges', min_value=0.0, format='%f')
            TotalCharges = st.number_input('Total Charges', min_value=0.0, format='%f')

        submitted = st.form_submit_button("Predict")
        if submitted:
            customer_data = {
                'gender': gender, 'SeniorCitizen': SeniorCitizen, 'Partner': Partner, 'Dependents': Dependents,
                'tenure': tenure, 'PhoneService': PhoneService, 'MultipleLines': MultipleLines,
                'InternetService': InternetService, 'OnlineSecurity': OnlineSecurity, 'OnlineBackup': OnlineBackup,
                'DeviceProtection': DeviceProtection, 'TechSupport': TechSupport, 'StreamingTV': StreamingTV,
                'StreamingMovies': StreamingMovies, 'Contract': Contract, 'PaperlessBilling': PaperlessBilling,
                'PaymentMethod': PaymentMethod, 'MonthlyCharges': MonthlyCharges, 'TotalCharges': TotalCharges
            }
            predictions = predict_single(customer_data)
            save_prediction(customer_data, predictions)
            st.write("Prediction results:")
            for model, prob in predictions.items():
                st.write(f"{model}: {'Churn' if prob > 0.5 else 'Not Churn'} with probability {prob:.2f}")

    st.header("Bulk Prediction")
    uploaded_file = st.file_uploader("Upload CSV", type='csv')
    if uploaded_file is not None:
        data_to_predict = pd.read_csv(uploaded_file)
        processed_data = preprocessor.transform(data_to_predict)
        bulk_predictions = {name: model.predict_proba(processed_data)[:, 1] for name, model in tuned_models.items()}
        st.write("Bulk prediction results:")
        for model, probs in bulk_predictions.items():
            st.write(f"{model} predictions:")
            st.write(probs)
        # Optionally save or provide download link for the predictions

if __name__ == "__main__":
    show()
