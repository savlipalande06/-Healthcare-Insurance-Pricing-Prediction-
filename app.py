import streamlit as st
import pickle
import pandas as pd
import numpy as np

def load_model():
    with open("best_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# Load trained model
model = load_model()

# Streamlit UI
st.title("Healthcare Pricing Prediction App")
st.write("Enter details to predict insurance charges.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=1)
sex = st.selectbox("Sex", ["Male", "Female"])
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Southwest", "Southeast", "Northwest", "Northeast"])

# Encode categorical variables
sex_encoded = 1 if sex == "Male" else 0
smoker_encoded = 1 if smoker == "Yes" else 0
region_mapping = {"Southwest": 0, "Southeast": 1, "Northwest": 2, "Northeast": 3}
region_encoded = region_mapping[region]

# Predict button
if st.button("Predict Charges"):
    input_data = np.array([[age, bmi, children, sex_encoded, smoker_encoded, region_encoded]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:.2f}")
