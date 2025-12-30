from fastapi import FastAPI
from pydantic import BaseModel
import joblib  # Import this!
import numpy as np

app = FastAPI()

# 1. Load the Model at Startup
# This happens once when the server turns on.
model = joblib.load('model_v1.pkl')

class HouseFeatures(BaseModel):
    rooms: int
    area_sqft: float

@app.post("/predict")
def predict_price(features: HouseFeatures):
    
    # Prepare data for the model (needs to be a 2D array)
    features_array = np.array([[features.rooms, features.area_sqft]])
    
    # 2. Ask the Real Model
    prediction = model.predict(features_array)
    
    return {"predicted_price": float(prediction[0])}