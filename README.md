# Housing Price Predictor
A simple and interactive web application built with Streamlit that estimates the price of a house based on user-input features using a pre-trained machine learning model.

## Features
1.Input key house features: living area, number of bathrooms, bedrooms, lot size, house age, and presence of fireplace.

2.Predict estimated house price instantly.

3.Visual feedback with a price range caption based on the prediction.

4.User-friendly interface with a sidebar for inputs and clean output display.

5.Includes a progress bar to visually represent the predicted price relative to a maximum threshold.

## How to Use

--------->Enter the house features on the sidebar.

--------->Click the Predict Price button.

View the estimated price and a descriptive caption indicating the house category (Cozy Small House, Comfortable Family Home, or Luxurious Mansion).

Optional: Visualize your input features as a bar chart and the price prediction as a progress bar.

## Tech Stack
----->1.Python

----->2.Streamlit for UI

----->3.Scikit-learn (model built with a Random Forest regressor)

----->4.Joblib for model serialization

## Setup and Run
Clone the repository
### Install dependencies:

pip install -r requirements.txt

## Run the app:

streamlit run app.py

### Notes

1.The model (random_forest_model.pkl) must be in the same directory as the app.

2.Modify the price thresholds and images (if used) to suit your dataset or region.

![image](https://github.com/user-attachments/assets/cd188ac7-81b3-46bd-945a-b9e417758edc)

![image](https://github.com/user-attachments/assets/0e06071b-d1d3-4700-8527-8df835a505de)


