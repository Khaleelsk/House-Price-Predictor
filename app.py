import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("random_forest_model.pkl")

# Page config
st.set_page_config(page_title="Housing Price Predictor", page_icon="🏠", layout="centered")

# Title
st.markdown("""
# Housing Price Predictor
### Get an estimated price based on your home's features
""")

# Sidebar for inputs
st.sidebar.header("🔧 Input House Features")

living_area = st.sidebar.number_input("📐 Living Area (sqft)", min_value=100)
bathrooms = st.sidebar.number_input("🚿 Number of Bathrooms", min_value=1.0, step=1.0)
bedrooms = st.sidebar.number_input("🛏️ Number of Bedrooms", min_value=1)
lot_size = st.sidebar.number_input("🌳 Lot Size", min_value=100.0)
age = st.sidebar.number_input("🏚️ Age of the House (Years)", min_value=0)
fireplace = st.sidebar.radio("🔥 Fireplace", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Prepare input data
input_data = pd.DataFrame([[living_area, bathrooms, bedrooms, lot_size, age, fireplace]],
                          columns=["LivingArea", "Bathrooms", "Bedrooms", "LotSize", "Age", "Fireplace"])

# Show input features bar chart
st.subheader("🏠 Your Input Features")
st.bar_chart(input_data.T, height=200)

# Predict button
if st.button("💰 Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏷️ Estimated House Price: ₹{prediction:,.2f}")
    st.balloons()

    # Visualize predicted price as a progress bar out of max assumed price (e.g., 50 million)
    max_price = 50000000
    progress = min(prediction / max_price, 1.0)
    st.subheader("💵 Price Range Indicator")
    st.progress(progress)

    # Show house image based on price range
    if prediction < 5000000:
        st.write("🏠 Cozy Small House")
    elif prediction < 15000000:
        st.write("🏡 Comfortable Family Home")
    else:
        st.write("🏰 Luxurious Mansion")

    # Simulate historical price data for a histogram (optional)
    st.subheader("📊 Price Distribution (Simulated)")
    import numpy as np
    simulated_prices = np.random.normal(loc=10000000, scale=4000000, size=1000)
    fig, ax = plt.subplots()
    ax.hist(simulated_prices, bins=30, color='skyblue', edgecolor='black')
    ax.axvline(prediction, color='red', linestyle='--', label="Your Predicted Price")
    ax.legend()
    st.pyplot(fig)
