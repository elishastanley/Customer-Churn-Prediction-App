def app():
    import streamlit as st
    import pandas as pd

    st.title('Prediction History')

    # Example DataFrame of historical data
    data = {
        'Date': ['2021-01-01', '2021-01-02'],
        'Input1': [123, 234],
        'Input2': [345, 456],
        'Prediction': ['Yes', 'No'],
        'Probability': [0.92, 0.86]
    }
    history_df = pd.DataFrame(data)

    st.dataframe(history_df)

    st.write("Review the history of predictions made through the app.")
