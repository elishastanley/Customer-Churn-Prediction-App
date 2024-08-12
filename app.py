import streamlit as st
from pages import home, data, dashboard, predict, history

page = st.sidebar.selectbox('Navigate', ['Home', 'Data', 'Dashboard', 'Predict', 'History'])

# Loading different pages based on selection
if page == 'Home':
    home.show()
elif page == 'Data':
    data.show()
elif page == 'Dashboard':
    dashboard.show()
elif page == 'Predict':
    predict.show()
elif page == 'History':
    history.show()
