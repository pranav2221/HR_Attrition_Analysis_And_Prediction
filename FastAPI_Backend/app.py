from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load models
lr_model = joblib.load("MODELS/logistic_model.pkl")
dt_model = joblib.load("MODELS/decision_tree.pkl")
rf_model = joblib.load("MODELS/random_forest.pkl")
scaler = joblib.load("MODELS/scaler.pkl")

app = FastAPI(title="HR Attrition Prediction API")

# ----------------------------
# Input Schemas
# ----------------------------
class EmployeeData(BaseModel):
    Age: int
    MonthlyIncome: int
    JobSatisfaction: int
    WorkLifeBalance: int
    YearsAtCompany: int
    OverTime: int  # 1 = Yes, 0 = No


@app.get("/")
def home():
    return {"message": "HR Attrition Ensemble Prediction API is running"}


# ----------------------------
# Helper: Risk Explanation
# ----------------------------
def generate_explanation(data: EmployeeData):
    reasons = []

    if data.YearsAtCompany <= 2:
        reasons.append("Early career employee")

    if data.OverTime == 1:
        reasons.append("Working overtime")

    if data.JobSatisfaction <= 2:
        reasons.append("Low job satisfaction")

    if data.WorkLifeBalance <= 2:
        reasons.append("Poor work-life balance")

    if data.MonthlyIncome < 4000:
        reasons.append("Low monthly income")

    if not reasons:
        reasons.append("No strong attrition risk factors detected")

    return reasons


# ----------------------------
# Prediction Endpoint
# ----------------------------
@app.post("/predict")
def predict(employee: EmployeeData):

    # Prepare input
    input_data = np.array([[ 
        employee.Age,
        employee.MonthlyIncome,
        employee.JobSatisfaction,
        employee.WorkLifeBalance,
        employee.YearsAtCompany,
        employee.OverTime
    ]])

    # Logistic Regression (scaled)
    input_scaled = scaler.transform(input_data)
    lr_prob = lr_model.predict_proba(input_scaled)[0][1]
    lr_pred = 1 if lr_prob >= 0.25 else 0

    # Decision Tree
    dt_prob = dt_model.predict_proba(input_data)[0][1]
    dt_pred = 1 if dt_prob >= 0.25 else 0

    # Random Forest
    rf_prob = rf_model.predict_proba(input_data)[0][1]
    rf_pred = 1 if rf_prob >= 0.25 else 0

    # ----------------------------
    # Ensemble Decision (Majority Vote)
    # ----------------------------
    votes = lr_pred + dt_pred + rf_pred

    final_risk = "High" if votes >= 2 else "Low"
    avg_probability = round(float((lr_prob + dt_prob + rf_prob) / 3), 4)

    # ----------------------------
    # Build Response
    # ----------------------------
    response = {
        "individual_predictions": {
            "logistic_regression": {
                "risk": "High" if lr_pred == 1 else "Low",
                "probability": round(float(lr_prob), 4)
            },
            "decision_tree": {
                "risk": "High" if dt_pred == 1 else "Low",
                "probability": round(float(dt_prob), 4)
            },
            "random_forest": {
                "risk": "High" if rf_pred == 1 else "Low",
                "probability": round(float(rf_prob), 4)
            }
        },
        "final_decision": {
            "ensemble_risk": final_risk,
            "average_probability": avg_probability,
            "decision_logic": "Majority voting among three models"
        },
        "explanation": {
            "top_risk_factors": generate_explanation(employee)
        }
    }

    return response
