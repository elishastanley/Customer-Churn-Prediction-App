def app():
    import streamlit as st
    from database import get_data

    st.title('Data Overview')

    # Adjust your SQL query as needed
    data_query = "SELECT * FROM your_table LIMIT 100"
    data = get_data(data_query)

    st.dataframe(data)

    st.write("Here you can explore the data collected in our database.")
