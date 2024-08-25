import streamlit as st
from database import get_prediction_history

st.set_page_config(
    page_title="Prediction History",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def show_history_page():
    st.title("Prediction History")
    df = get_prediction_history()
    st.dataframe(df.drop(columns=['id']))


if __name__ == "__main__":
    show_history_page()
