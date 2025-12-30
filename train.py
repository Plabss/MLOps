import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np
import mlflow
import mlflow.sklearn

# 1. Start the Experiment
mlflow.set_experiment("house-price-experiment")

# Dummy Data
X_train = np.array([[1, 500], [2, 1000], [3, 1500], [4, 2000], [5, 2500]])
y_train = np.array([100000, 200000, 300000, 400000, 500000])

# Start the 'Run' (like starting a stopwatch)
with mlflow.start_run():
    
    # Define parameters (useful to track what settings you used)
    params = {"model_type": "LinearRegression"}
    mlflow.log_params(params)
    
    # Train
    print("Training model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict to test accuracy
    predictions = model.predict(X_train)
    
    # Calculate Error (MAE)
    mae = mean_absolute_error(y_train, predictions)
    print(f"Mean Absolute Error: {mae}")
    
    # 2. Log the Metric (The Score)
    mlflow.log_metric("mae", mae)
    
    # 3. Log the Model (The Artifact)
    # MLflow handles the saving/pickling for us automatically!
    mlflow.sklearn.log_model(model, "my_model")
    
    print("Run complete. Check MLflow UI.")