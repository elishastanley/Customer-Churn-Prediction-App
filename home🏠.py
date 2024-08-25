import streamlit as st


def show():
    st.set_page_config(page_title="Customer Retention Analyzer",
                       page_icon="", layout="wide")
    st.title("Welcome to the Customer Retention Analyzer")

    container = st.container()
    col1, col2 = container.columns([5, 1])

    # Documentation and Details about the Application
    with col1:
        # Display the churn image
        st.image("Static/images/churn.png",
                 caption="Understanding Customer Churn", width=700)

        with st.expander("### About the Application", expanded=False):
            st.markdown("#### Customer Retention Analyzer")
            st.write("""
                The Customer Retention Analyzer is designed to predict whether a customer is likely to leave the service based on a variety of factors. This tool aids companies in implementing proactive retention strategies.
            """)

            st.markdown("#### Key Features")
            st.write("""
                - **View Data**: Accessed data in a remote database via connection.
                - **Dashboard**: Contains data visualizations to explore trends.
                - **Predict**: Make real-time predictions with machine learning models.
            """)

            st.markdown("#### User Benefits")
            st.write("""
                - Make data-driven decisions effortlessly.
                - Harness the power of machine learning without the complexity.
                - Save and analyze your data securely.
            """)

            st.markdown("#### Machine Learning Integration")
            st.write("""
                The application allows you to select between multiple predictive models, providing flexibility and accuracy in forecasts.
            """)

            st.markdown("#### Documentation")
            st.write("""
                This section documents the app's features, benefits, and machine learning integration, serving as a guide for users and developers alike.
            """)

    with col2:
        st.markdown("#### 🔗 Quick Links")
        st.write("""
            - [GitHub Repository](https://github.com/elishastanley/Churn-Prediction-Enhancing-Retention-with-Machine-Learning)
            - [LinkedIn Profile](https://www.linkedin.com/in/elisha-stanley/)
            - [Read on Medium](https://medium.com/@elishastanley255)
        """)

        st.markdown("##### 🤝 Connect with Me")
        st.write("""
            - [GitHub](https://github.com/elishastanley)
            - [LinkedIn](https://www.linkedin.com/in/elisha-stanley/)
            - [Medium](https://medium.com/@elishastanley255)
            - Contact me at [Email](mailto:elishastanley255@gmail.com)
        """)


if __name__ == "__main__":
    show()
