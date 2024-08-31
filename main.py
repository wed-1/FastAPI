from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()


# Load the pre-trained model
model = joblib.load('Models/linearR_model.pkl')

class PlayerData(BaseModel):
    appearance: int
    minutes_played: int
    award: int
    current_value: int
    highest_value: int

def preprocessing(input_data: PlayerData):
    # Convert input data to a numpy array
    features = np.array([
        input_data.appearance,
        input_data.minutes_played,
        input_data.award,
        data.current_value,
        input_data.highest_value
    ]).reshape(1, -1)  # Reshape for a single prediction
    return features


@app.post("/predict")
def predict(input_data: PlayerData):
    try:
        features = preprocessing(input_data)
        prediction = model.predict(features)
        return {"pred": prediction[0]}
    except Exception as e:
        return {"error": str(e)}

# Optional: A simple endpoint to check if the API is running
@app.get("/")
def root():
    return {"message": "Player Value Prediction."}
