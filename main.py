from fastapi import FastAPI
from pydantic import BaseModel
import logging
import json
from datetime import datetime

# 1. Setup the Logger
# We tell it to print information (INFO) to the console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mlops-logger")

app = FastAPI()

class HouseFeatures(BaseModel):
    rooms: int
    area_sqft: float

def fake_model_predict(rooms, area):
    price = (rooms * 10000) + (area * 150)
    return price

@app.post("/predict")
def predict_price(features: HouseFeatures):
    
    # Run the model
    prediction = fake_model_predict(features.rooms, features.area_sqft)
    
    # 2. Create the Log Record (The Black Box Data)
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "inputs": features.dict(),
        "prediction": prediction
    }
    
    # 3. Print the log as a JSON string
    # This will show up in your Render dashboard
    logger.info(json.dumps(log_data))
    
    return {"predicted_price": prediction}