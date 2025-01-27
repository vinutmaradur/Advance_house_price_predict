import streamlit as st
import pandas as pd
import numpy as np
import joblib  # To load the model

# Load the pre-trained model (ensure you have a trained model saved as 'model.pkl')
MODEL_PATH = "lr.pkl"  # Replace with your saved model path

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_data():
    # Load the dataset
    return pd.read_csv("USA_Housing.csv")

def predict_price(input_data):
    # Predict the price using the model
    lr = load_model()
    prediction = lr.predict(input_data)
    return prediction

# Streamlit UI
st.title("Advanced House Price Prediction")
st.write("This app predicts house prices using the USA Housing dataset.")

# Load the data
data = load_data()

# Display dataset info
if st.checkbox("Show Dataset Information"):
    st.write(data.head())
    st.write("Dataset Shape:", data.shape)
    st.write("Columns:", data.columns.tolist())

# Input fields
st.header("Enter House Features")
col1, col2 = st.columns(2)

with col1:
    avg_income = st.number_input("Average Income (in $)", min_value=0.0, value=50000.0, step=1000.0)
    avg_age = st.number_input("Average Age (in years)", min_value=0.0, value=30.0, step=1.0)

with col2:
    num_rooms = st.number_input("Number of Rooms", min_value=0.0, value=5.0, step=1.0)
    num_bedrooms = st.number_input("Number of Bedrooms", min_value=0.0, value=3.0, step=1.0)

area_population = st.number_input("Area Population", min_value=0.0, value=30000.0, step=1000.0)

# Prepare input data for prediction
input_features = pd.DataFrame({
    'Avg. Area Income': [avg_income],
    'Avg. Area House Age': [avg_age],
    'Avg. Area Number of Rooms': [num_rooms],
    'Avg. Area Number of Bedrooms': [num_bedrooms],
    'Area Population': [area_population]
})

# Predict button
if st.button("Predict House Price"):
    prediction = predict_price(input_features)
    st.success(f"The predicted house price is: ${prediction[0]:,.2f}")
