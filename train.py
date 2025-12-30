import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Create dummy data (The "Study Material")
# X = [rooms, area_sqft]
X_train = np.array([
    [1, 500],
    [2, 1000],
    [3, 1500],
    [4, 2000],
    [5, 2500]
])

# y = prices
y_train = np.array([100000, 200000, 300000, 400000, 500000])

# 2. Train the model (The "Learning")
print("Training model...")
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Save the model (The "Freezing")
# We save it as a file named 'model_v1.pkl'
joblib.dump(model, 'model_v1.pkl')
print("Model saved as model_v1.pkl")