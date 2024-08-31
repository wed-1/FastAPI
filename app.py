import streamlit as st
import requests
import json

# Set the page configuration
st.set_page_config(page_title="Player Value Prediction", layout="wide")

# Add a header with a subheader
st.title("Player Value Prediction :soccer:")

st.subheader("Predict the market value of a player based on various metrics")

# Create columns for input elements
col1, col2 = st.columns(2)

with col1:
    appearance = st.number_input("Number of Appearances", min_value=0, max_value=96, value=10, step=1)
    minutes_played = st.number_input("Minutes Played", min_value=0, max_value=8581, value=500, step=1)
    award = st.number_input("Number of Awards", min_value=0, max_value=92, value=1, step=1)
    highest_value = st.number_input("Highest Value ", min_value=0, max_value=18000000, value=500, step=100)
    current_value = st.number_input("Current Value (€)", min_value=0, max_value=180000, value=500, step=100)




# Create a dictionary for input data
input_data = {
    "appearance": appearance,
    "minutes_played": minutes_played,
    "award": award,
    "highest_value": highest_value,
    "current_value": current_value,

    
}
# Add a button for prediction
if st.button('Predict Player Value'):
    try:
        # Sending a POST request to the prediction API
        response = requests.post(
            url="https://fastapi-3-fony.onrender.com/predict",  # Ensure this is the correct endpoint
            headers={"Content-Type": "application/json"},
            data=json.dumps(input_data)
        )
        response.raise_for_status()  # Raise HTTP errors if any

        prediction = response.json().get('pred')
        st.success(f"Predicted Value: {prediction}")

    except requests.exceptions.RequestException as http_error:
        st.error(f"HTTP Request Error: {http_error}")
    except ValueError as json_error:
        st.error(f"JSON Parsing Error: {json_error}")
