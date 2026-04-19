# 🏦 Loan Approval Prediction System

🚀 A Machine Learning project that predicts whether a loan application will be approved based on applicant details, with an interactive Streamlit web application.

---

## 📌 Overview

Loan approval is a critical decision in the banking sector, requiring analysis of multiple financial and personal factors.  
This project builds a predictive model that determines the likelihood of loan approval using historical applicant data.

The system provides real-time predictions through an interactive user interface.

---

## 🎯 Objective

- Predict loan approval status using machine learning  
- Build a production-style ML pipeline  
- Provide an interactive UI for user input and prediction  

---

## 🧠 Model Details

- Model: **Random Forest Classifier**
- Framework: **Scikit-learn**
- Preprocessing:
  - Label Encoding for categorical variables  
  - StandardScaler for feature scaling  
- Evaluation Metric:
  - Accuracy Score  

---

## ⚙️ Workflow

1. Data Cleaning (handling missing values)  
2. Feature Engineering  
3. Encoding categorical variables  
4. Feature Scaling  
5. Model Training (Random Forest)  
6. Model Evaluation  
7. Model Saving (`model.pkl`, `scaler.pkl`, `encoders.pkl`)  
8. Deployment using Streamlit  

---

## 📊 Results

- Accuracy: **~80–85%**  
- Model provides probability-based prediction  
- Credit history is a key factor influencing loan approval  

---

## 🧪 Features

- ✅ End-to-end ML pipeline  
- ✅ Separate training and deployment scripts  
- ✅ Interactive user input via Streamlit  
- ✅ Probability-based decision making  
- ✅ Model persistence using `joblib`  

---

## 💻 How It Works

- User enters applicant details  
- Data is encoded and scaled using saved preprocessors  
- Model predicts approval probability  
- Output displays:
  - Approval / Rejection  
  - Probability score  

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Train the model (optional)

```bash
python train.py
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```
----

## 📂 Project Structure

loan-approval-prediction/
│
├── train.py         # Model training script
├── app.py           # Streamlit app
├── model.pkl        # Trained model
├── scaler.pkl       # Saved scaler
├── encoders.pkl     # Saved encoders
├── train_u6lujuX_CVtuZ9i.csv  # Dataset
├── requirements.txt
├── README.md

---

## 💡 Key Insights
 * Credit history plays a major role in loan approval
 * Feature scaling improves model performance
 * Random Forest handles complex relationships effectively
 * Separating training and deployment improves efficiency

---

## ⚠️ Disclaimer

This application is for educational purposes only and should not be used for real financial decisions.

---

## 🚀 Future Improvements
 
 * Add ROC-AUC and confusion matrix visualization
 * Use advanced models (XGBoost, LightGBM)
 * Deploy using Streamlit Cloud
 * Improve UI/UX design

---

💼 Applications

 * Banking and financial services
 * Loan risk assessment
 * Credit scoring systems
 * Decision support tools

---

## 👨‍💻 Author

Khaja Pasha

GitHub: https://github.com/khajapashas722-alt
