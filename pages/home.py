import streamlit as st

def show():
    st.set_page_config(page_title="Churn Prediction App", page_icon="🔄", layout="wide")

    st.title("Welcome to the Churn Prediction Application")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.image("Static/images/churn.png", width=800)  # Adjust the width to fit the content appropriately
        st.header("📘 About the Application")
        st.write(
            """
            This application is designed to predict customer churn using machine learning techniques. 
            It helps businesses understand customer behavior and improve retention strategies. 
            By analyzing historical data, this application provides insights into factors contributing to customer churn.
            """
        )

    with col2:
        st.header("🔗 Quick Links")
        st.markdown(
            """
            - **GitHub Repository**: [Visit GitHub](https://github.com/elishastanley/Churn-Prediction-Enhancing-Retention-with-Machine-Learning)
            - **LinkedIn Profile**: [Visit LinkedIn](https://www.linkedin.com/in/elishastanley)
            - **Read on Medium**: [Visit Medium](https://medium.com/@elishastanley)
            """,
            unsafe_allow_html=True
        )
        
        st.header("🤝 Connect with Me")
        st.markdown(
            """
            - [GitHub](https://github.com/elishastanley) 👨‍💻
            - [LinkedIn](https://www.linkedin.com/in/elishastanley) 🖇️
            - [Medium](https://medium.com/@elishastanley) 📘
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <hr style='margin-top: 2rem; margin-bottom: 1rem;'>
        <footer style='text-align: center; color: grey;'>
            <p>Churn Prediction Application</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    show()
