import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Generate dummy dataset for demand prediction
# Columns: Product ID, Month, Demand
data = {
    "ProductID": [1, 1, 1, 2, 2, 2, 3, 3, 3],
    "Month": [1, 2, 3, 1, 2, 3, 1, 2, 3],
    "Demand": [100, 120, 130, 80, 85, 90, 200, 210, 220]
}
df = pd.DataFrame(data)

# Prepare features (X) and target (y)
X = df[["ProductID", "Month"]]
y = df["Demand"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file
model_filename = "ai_models/demand_predictor.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(model, file)

print(f"Model has been trained and saved to {model_filename}")
