import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Title and description
st.title('Advanced House Price Prediction')
st.write("This app predicts house prices using the USA_Housing dataset.")

# Load the dataset
def load_data():
    try:
        data = pd.read_csv("USA_Housing.csv")
        return data
    except FileNotFoundError:
        st.error("USA_Housing.csv file not found. Please ensure the file is in the correct location.")
        return None

data = load_data()
if data is not None:
    st.write("### Dataset Preview")
    st.write(data.head())

    # Prepare data for training
    X = data.drop(['Price', 'Address'], axis=1)  # Features (excluding 'Price' and 'Address')
    y = data['Price']  # Target variable

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    st.write("### Training the Model")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    st.write(f"Model Performance: RMSE = {rmse:.2f}")

    # Input for prediction
    st.write("### Predict House Price")
    avg_area_income = st.number_input("Average Area Income", value=50000.0)
    avg_area_house_age = st.number_input("Average Area House Age", value=5.0)
    avg_area_number_of_rooms = st.number_input("Average Area Number of Rooms", value=5.0)
    avg_area_number_of_bedrooms = st.number_input("Average Area Number of Bedrooms", value=3.0)
    area_population = st.number_input("Area Population", value=20000.0)

    # Predict button
    if st.button("Predict Price"):
        input_data = pd.DataFrame({
            'Avg. Area Income': [avg_area_income],
            'Avg. Area House Age': [avg_area_house_age],
            'Avg. Area Number of Rooms': [avg_area_number_of_rooms],
            'Avg. Area Number of Bedrooms': [avg_area_number_of_bedrooms],
            'Area Population': [area_population]
        })

        prediction = model.predict(input_data)[0]
        st.write(f"### Predicted House Price: ${prediction:,.2f}")
