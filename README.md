📊 HR Attrition Analysis & Prediction System

An end-to-end data analytics and machine learning project that analyzes employee attrition patterns and predicts attrition risk using an ensemble of models. 
The project also includes an interactive Streamlit web application for real-time predictions.

🔍 Problem Statement

Employee attrition leads to increased hiring costs, loss of experienced talent, and reduced productivity. 
Organizations often struggle to identify employees who are at risk of leaving at an early stage.

This project aims to:

Analyze key factors influencing employee attrition

Build predictive models to identify high-risk employees

Provide an interactive tool for HR teams to make proactive retention decisions

🎯 Project Objectives

Perform data cleaning and exploratory data analysis (EDA)

Extract business insights using SQL

Build and evaluate machine learning models

Create interactive dashboards for visualization

Deploy a user-friendly web application for real-time prediction

🧠 Solution Overview

The system predicts employee attrition risk using an ensemble of machine learning models:

Logistic Regression

Decision Tree

Random Forest

A majority-voting ensemble strategy is used for final decision-making, along with explainable risk factors to support HR decision-making.

🛠️ Tech Stack
Programming & Analysis

Python

Pandas, NumPy

Scikit-learn

Data & Visualization

SQL (MySQL / PostgreSQL)

Power BI

Machine Learning

Logistic Regression

Decision Tree

Random Forest

Ensemble Learning

Deployment & UI

Streamlit (Frontend & Deployment)

FastAPI (Backend – local & architectural layer)

Git & GitHub

📁 Project Structure
HR_Attrition_Analysis_And_Prediction/
│
├── Datasets/
│   ├── HR_Attrition_Original.csv
│   └── HR_Attrition_SQL.csv
│
├── FastAPI_Backend/
│   └── app.py
│
├── Jupyter_Notebooks/
│   ├── HR_Employee_Attrition_EDA.ipynb
│   └── Prediction_Model.ipynb
│
├── SQL_Analysis/
│   └── HR_Attrition.sql
│
├── PowerBI_Dashboard/
│   └── HR_ATTRITION_ANALYSIS_Dashboard.pbix
│
├── models/
│   ├── decision_tree.pkl
│   ├── logistic_model.pkl
│   ├── random_forest.pkl
│   └── scaler.pkl
│
├── .gitignore
├── README.md
├── requirements.txt
└── streamlit_app.py


📊 Key Insights from Analysis

Highest attrition occurs in the early years of employment

Overtime significantly increases attrition risk

Low job satisfaction and poor work-life balance are major drivers

Salary alone does not guarantee retention

Ensemble models provide more reliable predictions than a single model

🤖 Machine Learning Models
Model	Purpose
Logistic Regression	Interpretable baseline model
Decision Tree	Rule-based decision logic
Random Forest	Robust ensemble learner

Final Prediction Logic:
Majority voting among all three models
Threshold-based classification (High / Low risk)

🌐 Streamlit Web Application

The deployed Streamlit app allows users to:

Enter employee details via sliders and dropdowns

View individual model predictions

See the final ensemble decision

Understand key risk factors behind predictions

Sample Inputs

Age

Monthly Income

Job Satisfaction

Work-Life Balance

Years at Company

Overtime status

🚀 Deployment Strategy

The interactive application is deployed using Streamlit Cloud

Trained models are loaded directly into the Streamlit app

A FastAPI backend is included in the repository to demonstrate production-ready API design (used locally / for scalable deployment)

▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/<your-username>/HR-Attrition-Analysis-Prediction.git
cd HR-Attrition-Analysis-Prediction

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit app
streamlit run streamlit_app.py

🧪 Model Validation

The system was tested using:

High-risk employee profiles

Low-risk senior profiles

Borderline and contradictory cases

This ensured consistent predictions and meaningful explanations across scenarios.

📌 Use Cases

HR attrition risk assessment

Workforce planning and retention strategies

Employee engagement analysis

Learning reference for end-to-end ML projects

👤 Author

Pranav Patil
Aspiring Data Analyst / Machine Learning Enthusiast

🔗 GitHub: https://github.com/pranav2221

