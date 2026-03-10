
# Taxi Fare Prediction - Streamlit App

import streamlit as st
import pandas as pd
import joblib
import sys
import os

# allow python to find src folder
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# load trained model
model = joblib.load("model.pkl")

st.title(" Taxi Fare Prediction")

st.write("Enter trip details to predict taxi fare")


# User Inputs

pickup_datetime = st.datetime_input("Pickup Time")

dropoff_datetime = st.datetime_input("Dropoff Time")

passenger_count = st.number_input(
    "Passenger Count",
    min_value=1,
    max_value=6,
    value=1
)

trip_distance = st.number_input(
    "Trip Distance",
    min_value=0.0,
    value=1.0
)

RatecodeID = st.selectbox(
    "Rate Code",
    [1, 2, 3, 4, 5, 6]
)

payment_type = st.selectbox(
    "Payment Type",
    [1, 2, 3, 4]
)

extra = st.number_input(
    "Extra Charges",
    value=0.0
)

tip_amount = st.number_input(
    "Tip Amount",
    value=0.0
)

tolls_amount = st.number_input(
    "Tolls Amount",
    value=0.0
)
congestion_surcharge = st.number_input(
    "Congestion Surcharge",
    value=0.0
)

Airport_fee = st.number_input(
    "Airport Fee",
    value=0.0
)


# Create Input Data

input_data = pd.DataFrame({
    "tpep_pickup_datetime": [pickup_datetime],
    "tpep_dropoff_datetime": [dropoff_datetime],
    "passenger_count": [passenger_count],
    "trip_distance": [trip_distance],
    "RatecodeID": [RatecodeID],
    "payment_type": [payment_type],
    "extra": [extra],
    "tip_amount": [tip_amount],
    "tolls_amount": [tolls_amount],
    "congestion_surcharge": [congestion_surcharge],
    "Airport_fee": [Airport_fee]
})

# Prediction

if st.button("Predict Fare"):

    prediction = model.predict(input_data)

    st.success(f" Predicted Taxi Fare: ${prediction[0]:.2f}")