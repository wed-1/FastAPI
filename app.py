import streamlit as st
import requests
import json

# Set the page configuration
st.set_page_config(page_title="Player Value Prediction", page_icon="⚽", layout="wide")

# Add a header with a subheader
st.title("Player Value Prediction :soccer:")


# Create columns for input elements
col1, col2 = st.columns(2)

with col1:
    appearance = st.number_input("Number of Appearances", min_value=0, max_value=96, value=10, step=1)
    goals = st.number_input("Number of Goals", min_value=0, max_value=100, value=5, step=1)
    assists = st.number_input("Number of Assists", min_value=0, max_value=100, value=5, step=1)
    minutes_played = st.number_input("Minutes Played", min_value=0, max_value=8581, value=500, step=1)
    games_injured = st.number_input("Number of Games Injured", min_value=0, max_value=100, value=0, step=1)
    award = st.number_input("Number of Awards", min_value=0, max_value=92, value=1, step=1)
    highest_value = st.number_input("Highest Value ", min_value=0, max_value=180000, value=500, step=100)



# Create a dictionary for input data
input_data = {
    "appearance": appearance,
    "goals": goals,
    "assists": assists,
    "minutes_played": minutes_played,
    "games_injured": games_injured,
    "award": award,
    "highest_value": highest_value,
    
}

# Add a button for prediction
if st.button('Predict Player Value'):
    try:
        # Sending a POST request to the prediction API
        response = requests.post(
            url="https://use-case-7-18ry.onrender.com/predict",  # Update this with your actual deployed URL
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

# Add some information about the app or prediction model at the bottom
