import streamlit as st
import numpy as np
import joblib

# ---------------------------
# Load Models
# ---------------------------
lr_model = joblib.load("models/logistic_model.pkl")
dt_model = joblib.load("models/decision_tree.pkl")
rf_model = joblib.load("models/random_forest.pkl")
scaler = joblib.load("models/scaler.pkl")

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="HR Attrition Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 HR Attrition Prediction System")
st.write(
    "Interactive system to predict employee attrition risk using an ensemble of ML models."
)

# ---------------------------
# Input Form
# ---------------------------
with st.form("attrition_form"):

    age = st.slider("Age", 18, 60, 28)

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=20000,
        value=3500,
        step=500
    )

    years_at_company = st.slider("Years at Company", 0, 40, 1)

    job_satisfaction = st.selectbox(
        "Job Satisfaction (1 = Low, 4 = High)", [1, 2, 3, 4], index=1
    )

    work_life_balance = st.selectbox(
        "Work Life Balance (1 = Poor, 4 = Excellent)", [1, 2, 3, 4], index=1
    )

    overtime = st.radio("Works Overtime?", ["Yes", "No"])
    overtime_val = 1 if overtime == "Yes" else 0

    submit = st.form_submit_button("🔍 Predict Attrition Risk")

# ---------------------------
# Prediction Logic
# ---------------------------
if submit:

    input_data = np.array([[ 
        age,
        monthly_income,
        job_satisfaction,
        work_life_balance,
        years_at_company,
        overtime_val
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

    # Ensemble
    votes = lr_pred + dt_pred + rf_pred
    final_risk = "High" if votes >= 2 else "Low"
    avg_prob = round(float((lr_prob + dt_prob + rf_prob) / 3), 4)

    # ---------------------------
    # Results
    # ---------------------------
    st.success("Prediction completed successfully!")

    st.subheader("🧠 Final Ensemble Decision")
    st.write(f"**Attrition Risk:** {final_risk}")
    st.write(f"**Average Probability:** {avg_prob}")

    st.subheader("📈 Individual Model Predictions")

lr_risk = "High" if lr_prob >= 0.25 else "Low"
dt_risk = "High" if dt_prob >= 0.25 else "Low"
rf_risk = "High" if rf_prob >= 0.25 else "Low"

st.write(
    f"**Logistic Regression** → Risk: **{lr_risk}**, Probability: {round(lr_prob,4)}"
)
st.write(
    f"**Decision Tree** → Risk: **{dt_risk}**, Probability: {round(dt_prob,4)}"
)
st.write(
    f"**Random Forest** → Risk: **{rf_risk}**, Probability: {round(rf_prob,4)}"
)

st.subheader("📝 Explanation")

reasons = []

if years_at_company <= 2:
    reasons.append("Early career employee")

if overtime_val == 1:
    reasons.append("Working overtime")

if job_satisfaction <= 2:
    reasons.append("Low job satisfaction")

if work_life_balance <= 2:
    reasons.append("Poor work-life balance")

if monthly_income < 4000:
    reasons.append("Low monthly income")

# ✅ IMPORTANT: Always show at least one explanation
if not reasons:
    reasons.append("No strong attrition risk factors detected")

# Display explanations
for reason in reasons:
    st.write(f"- {reason}")
