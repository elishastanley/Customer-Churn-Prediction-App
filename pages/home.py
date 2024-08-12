def app():
    import streamlit as st

    st.title('Welcome to Our Data Insights App!')

    st.image('path/to/your/logo_or_image.png', width=300)

    st.write("""
    This application provides a comprehensive suite of tools for data analysis, visualization, 
    and prediction. Explore different pages to interact with data, visualize trends, or make predictions.
    """)

    st.subheader('Quick Links')
    st.markdown("""
    - [GitHub Repository](https://github.com/yourgithub)
    - [LinkedIn Profile](https://linkedin.com/in/yourprofile)
    - [Medium Articles](https://medium.com/@yourusername)
    """)
