import streamlit as st
from database import get_prediction_history


def show_history_page():
    st.title("Prediction History")
    df = get_prediction_history()
    st.dataframe(df.drop(columns=['id']))


if __name__ == "__main__":
    show_history_page()
