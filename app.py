import streamlit as st
import numpy as np
import joblib

# Load saved files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("encoders.pkl")

st.title("🏦 Loan Approval Prediction")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_emp = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban","Semiurban","Rural"])

dependents = st.selectbox("Dependents", [0,1,2,3])

app_income = st.slider("Applicant Income", 0, 200000, 50000)
coapp_income = st.slider("Coapplicant Income", 0, 100000, 0)
loan_amt = st.slider("Loan Amount", 10, 700, 150)
loan_term = st.slider("Loan Term", 120, 480, 360)
credit_score = st.slider("Credit Score", 300, 900, 650)

credit_history = 1 if credit_score >= 600 else 0

# Encode
gender = encoders["Gender"].transform([gender])[0]
married = encoders["Married"].transform([married])[0]
education = encoders["Education"].transform([education])[0]
self_emp = encoders["Self_Employed"].transform([self_emp])[0]
property_area = encoders["Property_Area"].transform([property_area])[0]

# Predict
if st.button("Predict"):
    data = np.array([[app_income, coapp_income, loan_amt, loan_term,
                      credit_history, dependents,
                      gender, married, education, self_emp, property_area]])

    scaled = scaler.transform(data)
    prob = model.predict_proba(scaled)[0][1]

    if prob >= 0.4:
        st.success(f"✅ Loan Approved ({prob:.2f})")
    else:
        st.error(f"❌ Loan Rejected ({prob:.2f})")

st.info("Prediction is based on ML model and for educational purposes only.")
