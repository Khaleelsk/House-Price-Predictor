Housing Price Predictor
A simple and interactive web application built with Streamlit that estimates the price of a house based on user-input features using a pre-trained machine learning model.

Features
Input key house features: living area, number of bathrooms, bedrooms, lot size, house age, and presence of fireplace.

Predict estimated house price instantly.

Visual feedback with a price range caption based on the prediction.

User-friendly interface with a sidebar for inputs and clean output display.

Includes a progress bar to visually represent the predicted price relative to a maximum threshold.

How to Use
Enter the house features on the sidebar.

Click the Predict Price button.

View the estimated price and a descriptive caption indicating the house category (Cozy Small House, Comfortable Family Home, or Luxurious Mansion).

Optional: Visualize your input features as a bar chart and the price prediction as a progress bar.

Tech Stack
Python

Streamlit for UI

Scikit-learn (model built with a Random Forest regressor)

Joblib for model serialization

Setup and Run
Clone the repository

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
Notes
The model (random_forest_model.pkl) must be in the same directory as the app.

Modify the price thresholds and images (if used) to suit your dataset or region.
