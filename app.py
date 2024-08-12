import streamlit as st
from pages import home, data, dashboard, predict, history

PAGES = {
    "Home": home,
    "Data": data,
    "Dashboard": dashboard,
    "Predict": predict,
    "History": history
}


def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()


if __name__ == "__main__":
    main()
