from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the App (The Restaurant)
app = FastAPI()

# 2. Define the Data Format ( The Menu)
# This tells the user: "I need exactly these two numbers."
class HouseFeatures(BaseModel):
    rooms: int
    area_sqft: float

# 3. Load the Model (The Chef)
# (In real life, you would use: model = joblib.load("model.pkl"))
# Here we just use a simple function to simulate a model.
def fake_model_predict(rooms, area):
    price = (rooms * 10000) + (area * 150)
    return price

# 4. Create the Endpoint (The Waiter)
# 'POST' means the user is sending us data.
@app.post("/predict")
def predict_price(features: HouseFeatures):
    
    # Extract data from the request
    rooms = features.rooms
    area = features.area_sqft
    
    # Run the model
    prediction = fake_model_predict(rooms, area)
    
    # Return the result (JSON)
    return {"predicted_price": prediction}