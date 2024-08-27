import streamlit as st
from home import show as show_home
from data import show as show_data
from dashboard import show as show_dashboard
from predict import show as show_prediction
from history import show as show_history

# Simulated user database
users = {
    "admin": "admin123",
    "user": "user123"
}

# Authentication


def authenticate(username, password):
    return users.get(username) == password

# Main app logic


def main():
    if 'login_status' not in st.session_state:
        st.session_state['login_status'] = False

    if st.session_state['login_status']:
        if st.sidebar.button("Logout"):
            st.session_state['login_status'] = False
            st.sidebar.success("You have been logged out.")
            st.rerun()
    else:
        st.sidebar.title("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            if authenticate(username, password):
                st.session_state['login_status'] = True
                st.session_state['username'] = username
                st.rerun()
            else:
                st.sidebar.error("Incorrect Username/Password")

    if st.session_state.get('login_status'):
        st.sidebar.success(f"Logged in as {st.session_state['username']}")
        page = st.sidebar.radio(
            "Go to", ('Home', 'Data', 'Dashboard', 'Prediction', 'History'))
        if page == 'Home':
            show_home()
        elif page == 'Data':
            show_data()
        elif page == 'Dashboard':
            show_dashboard()
        elif page == 'Prediction':
            show_prediction()
        elif page == 'History':
            show_history()
    else:
        st.info("Please login to access the application")


if __name__ == "__main__":
    main()
