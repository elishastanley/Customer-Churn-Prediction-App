def app():
    import streamlit as st
    import plotly.express as px
    from database import get_data

    st.title('Interactive Data Dashboard')

    data_query = "SELECT column1, column2 FROM your_table"  # Adjust accordingly
    data = get_data(data_query)

    fig = px.bar(data, x='column1', y='column2', title="Sample Visualization")
    st.plotly_chart(fig)

    st.write("Use the dashboard to explore trends and patterns in the data.")
