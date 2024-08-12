def app():
    import streamlit as st
    from model import load_model, predict

    st.title('Prediction Tool')

    # Load your model (adjust the path)
    model = load_model('path/to/your_model.pkl')

    # Create input fields for user input
    input1 = st.number_input('Enter the first input')
    input2 = st.number_input('Enter the second input')

    if st.button('Predict'):
        # Assuming your model expects a numpy array
        prediction, probability = predict(model, [[input1, input2]])
        st.write(f'Prediction: {prediction[0]}')
        st.write(f'Probability: {probability.max()}')

    st.write("Input data to receive real-time predictions and their probabilities.")
