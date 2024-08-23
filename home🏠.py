import streamlit as st


def show():
    st.set_page_config(page_title="Churn Prediction App",
                       page_icon="", layout="wide")
    st.title("Welcome to the Churn Prediction Application")

    # Using a single container to manage all content more compactly
    container = st.container()
    col1, col2 = container.columns([5, 1])

    #st.image("Static/images/churn.png", width=400)

    with col1:    

        with st.expander("### About the Application", expanded=True):
            st.markdown("#### About the Application")
            st.write("""
                This application predicts customer churn using machine learning. It helps businesses improve retention strategies by providing insights into customer behavior.
            """)

            st.markdown("#### Introduction")
            st.write("""
                Understanding customer churn allows businesses to develop strategies to increase retention.
            """)


            st.markdown("#### Problem Statement and Goals")
            st.write("""
                The goal is to reduce customer churn by identifying at-risk customers and suggesting effective strategies.
            """)

            st.markdown("#### Data Understanding")
            st.write("""
                Utilizes data to predict churn based on attributes like gender, service usage, and billing methods.
            """)

            st.markdown("#### Hypotheses Testing")
            st.write("""
                Tests hypotheses on factors impacting churn, like differences in monthly charges.
            """)

            

    with col2:
        
        st.markdown("#### 🔗 Quick Links")
        st.write("""
            - [GitHub Repository](https://github.com/elishastanley/Churn-Prediction-Enhancing-Retention-with-Machine-Learning)
            - [LinkedIn Profile](https://www.linkedin.com/in/elishastanley)
            - [Read on Medium](https://medium.com/@elishastanley)
        """)

        st.markdown("##### 🤝 Connect with Me")
        st.write("""
            - [GitHub](https://github.com/elishastanley)
            - [LinkedIn](https://www.linkedin.com/in/elishastanley)
            - [Medium](https://medium.com/@elishastanley)
        """)


if __name__ == "__main__":
    show()
