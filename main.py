from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from huggingface_hub import hf_hub_download # New Import!

app = FastAPI()

# 1. Download and Load the Model at Startup
# Replace 'YOUR_HF_USERNAME' with your actual username!
MODEL_REPO = "plabs99/house-price-model"
MODEL_FILENAME = "model_v1.pkl"

print("Downloading model from Hugging Face...")
model_path = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILENAME)
model = joblib.load(model_path)
print("Model loaded successfully!")

class HouseFeatures(BaseModel):
    rooms: int
    area_sqft: float

@app.post("/predict")
def predict_price(features: HouseFeatures):
    features_array = np.array([[features.rooms, features.area_sqft]])
    prediction = model.predict(features_array)
    return {"predicted_price": float(prediction[0])}