from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import pickle
import os

app = Flask(__name__)

# Load AI Model
model_path = "ai_models/demand_predictor.pkl"
if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        demand_model = pickle.load(file)
else:
    demand_model = None

# Home route
@app.route("/")
def home():
    return render_template("login.html")

# Login route
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin":  # Replace with real authentication
        return redirect(url_for("dashboard"))
    else:
        return "Invalid login credentials", 401

# Dashboard route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Locate parts route
@app.route("/locate_parts")
def locate_parts():
    return render_template("locate_parts.html")

# Demand prediction route
@app.route("/demand_products", methods=["GET", "POST"])
def demand_products():
    if request.method == "POST":
        product_id = int(request.form["product_id"])
        month = int(request.form["month"])  # Ensure month is numeric
        if demand_model:
            prediction = demand_model.predict([[product_id, month]])[0]
            return jsonify({"prediction": prediction})
        else:
            return jsonify({"error": "AI model not loaded"}), 500
    return render_template("demand_products.html")

# Chatbot route
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
