import streamlit as st
import joblib
import numpy as np

model = joblib.load("regression.joblib")

st.title("House Price Prediction")

with st.form("house_form"):

    size = st.number_input("Size of the house (in square meters)", min_value=10.0, step=1.0)
    bedrooms = st.number_input("Number of bedrooms", min_value=1, step=1)
    garden = st.number_input("Does the house have a garden? (1 for Yes, 0 for No)", min_value=0, max_value=1, step=1)


    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = np.array([[size, bedrooms, garden]]) 
        prediction = model.predict(input_data)
        st.write(f"The predicted price of the house is: ${prediction[0]:,.2f}")
