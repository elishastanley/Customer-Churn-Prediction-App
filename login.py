import streamlit as st

# login form
with st.sidebar:
    st.header('Login')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.sidebar.write("Login Attempted")

st.markdown("### CHURN MANAGEMENT APP")
st.image("images/churn05.png", use_column_width=True)

