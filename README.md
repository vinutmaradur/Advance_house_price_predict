# Advanced House Price Prediction App 🏠

This repository contains a **Streamlit** application for predicting house prices using the **USA_Housing** dataset. 
The app leverages a **Random Forest Regressor** for predictions and provides an interactive interface to input data for customized price predictions.

---

## Features ✨

This section outlines what the app does. For your project:

- **Data Preview**: Users can see the first few rows of the dataset.
- **Model Training**: Explains that a Random Forest Regressor is trained.
- **Model Performance**: Evaluates and shows the performance of the model with RMSE (Root Mean Squared Error).
- **Custom Predictions**: Users can input custom values to predict a house's price.
This list tells users what they can expect from the app.

---

## Screenshots 🖼️

![img alt](https://github.com/vinutmaradur/Advance_house_price_predict/blob/main/hp%201.png?raw=true)
![img alt](https://github.com/vinutmaradur/Advance_house_price_predict/blob/main/hp%202.png?raw=true)
![img alt](https://github.com/vinutmaradur/Advance_house_price_predict/blob/main/hp%203.png?raw=true)
![img alt](https://github.com/vinutmaradur/Advance_house_price_predict/blob/main/hp%204.png?raw=true)

---

## About Dataset 📂

The USA_Housing.csv file contains data used for predicting house prices. Each row represents a specific area, with various attributes describing the area's characteristics. 
The dataset has the following columns:

# Features in the Dataset

| Column Name |	Description |	Data Type |
| :- | :- | :- |
| Avg. Area Income |	The average income of the residents in the area (in dollars). |	Numerical (float) |
| Avg. Area House Age |	The average age of the houses in the area (in years). |	Numerical (float) |
| Avg. Area Number of Rooms |	The average number of rooms in the houses within the area. |	Numerical (float) |
| Avg. Area Number of Bedrooms |	The average number of bedrooms in the houses within the area. |	Numerical (float) |
| Area Population |	The total population living in the area. |	Numerical (float) |
| Price |	The actual price of the house (in dollars) — this is the target variable for the prediction. |	Numerical (float) |
| Address |	The address of the house (not used in the prediction model, included for informational purposes). |	Categorical (string) |

# Purpose of the Dataset
The dataset is used to:

- **Train the Model**:
    - The features (Avg. Area Income, Avg. Area House Age, etc.) are used to predict the Price.
    - The Address column is excluded from the training, as it is not relevant for the prediction.
- **Test the Model**:
    - A portion of the data is used for testing the model to evaluate its performance.
- **Make Predictions**:
    - Once the model is trained, it uses user inputs (values for the features) to predict house prices.

# Dataset Example
Here’s a small preview of what the dataset looks like:

| Avg. Area Income |	Avg. Area House Age |	Avg. Area Number of Rooms |	Avg. Area Number of Bedrooms |	Area Population |	Price |	Address |
| :- | :- | :- | :- | :- | :- | :- |
| 79545.46 |	5.682861 |	7.009188 |	4.09 |	23086.80 |	1059033.55 |	208 Michael Ferry Rd. |
| 79248.63 |	6.002900 |	6.730821 |	3.09 |	40173.07 |	1505890.91 |	188 Johnson Ave. |

# File Requirements
- **File Name**: The dataset file must be named **USA_Housing.csv**.
- **Location**: The file should be placed in the root directory of the project so that the app can load it successfully.
- **Format**: The file must be in CSV (Comma-Separated Values) format.

# Data Preprocessing
Before training the model, the dataset undergoes preprocessing:

- The Price column is treated as the target variable (the value to be predicted).
- The Address column is excluded from the model since it is irrelevant for numerical prediction.
- The remaining columns (Avg. Area Income, Avg. Area House Age, etc.) are used as features for the prediction model.

# Input Features
1. Avg. Area Income
   - **Description**: Average income of the people in the area.
   - **Type**: Numerical (float).
   - **Example Value**: 50000.0 (in dollars).
     
2. Avg. Area House Age
    - **Description**: Average age of houses in the area (in years).
    - **Type**: Numerical (float).
    - **Example Value**: 5.0 (years).
      
3. Avg. Area Number of Rooms
    - **Description**: Average number of rooms in houses in the area.
    - **Type**: Numerical (float).
    - **Example Value**: 6.5.
      
4. Avg. Area Number of Bedrooms
    - **Description**: Average number of bedrooms in houses in the area.
    - **Type**: Numerical (float).
    - **Example Value**: 3.0.
      
5. Area Population
    - **Description**: Total population in the area.
    - **Type**: Numerical (float).
    - **Example Value**: 30000.0.
  
# Output Features
  - **Description**: The app predicts the estimated price of a house based on the input features.
  - **Type**: Numerical (float).
  - **Unit**: Dollars (formatted with commas).
  - **Example Value**: **$1,200,000.00**.

# Example Input-Output in the App
# Inputs:
  - **Avg. Area Income**: 60000.0
  - **Avg. Area House Age**: 5.5
  - **Avg. Area Number of Rooms**: 7.2
  - **Avg. Area Number of Bedrooms**: 4.0
  - **Area Population**: 40000.0
# Predicted Output:
  - **Predicted House Price**: **$1,500,000.00**

---

## Requirements 🛠️
To run the application, ensure the following dependencies are installed:
- `streamlit`
- `pandas`
- `scikit-learn`
- `numpy`

---

## How to Run 🚀

1. Clone the repository:

```bash
      git clone https://github.com/your-username/house-price-prediction-app.git
      cd house-price-prediction-app
```

2. Install the dependencies using:
```bash
    pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
    streamlit run app.py
```

4. Open the app:
     The command will give a local URL (e.g., http://localhost:8501) to access the app in your browser.

---

## App Workflow 📋
1. **Dataset Preview**: The app shows a preview of the data if the dataset is correctly loaded.
2. **Model Training**:
  - Splits the data into training and testing sets.
  - Trains a Random Forest Regressor model.
  - Displays the model's performance (RMSE).
3. **Price Prediction**:
- Users input:
   - Average Area Income
   - Average Area House Age
   - Average Number of Rooms and Bedrooms
   - Area Population
- The app predicts the house price based on the inputs.

---

## File Structure 📁
  ```bash
      ├── app.py                # Main Streamlit app
      ├── requirements.txt      # List of dependencies
      ├── USA_Housing.csv       # Dataset (must be added manually)
      └── README.md             # Project documentation
  ```

---

## Contributing 🤝
This section invites others to:

- Report issues with the app.
- Suggest new features or improvements.
- Contribute code via pull requests.
This is useful for collaborative projects.

---

## License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments 🙏
Special thanks to:

- Streamlit
- scikit-learn
- Pandas

---

## Check my code 👁️
Below is the link to check my app

  [Project demo](https://advancehousepricepredict-2025.streamlit.app/) 🚀

---
## Happy coding! 💻

Let me know if you’d like to customize any sections further!
