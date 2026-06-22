# 📡 Telecom Customer Churn AI

An Explainable AI powered Telecom Customer Churn Prediction System that predicts whether a customer is likely to leave and explains the reasons behind the prediction.

## 🚀 Live Demo

🔗 Streamlit App:

https://telecom-churn-aigit-jvwn8gwwl5vf2acqen85uu.streamlit.app/


## 📌 Features

✅ Customer churn prediction  
✅ Churn probability score  
✅ Explainable AI using SHAP  
✅ Customer risk analysis  
✅ Retention recommendations  
✅ Prediction history  
✅ Downloadable AI report  
✅ Interactive dashboard  


## 🧠 How It Works

The system uses Machine Learning to analyze customer information:

- Tenure
- Monthly charges
- Contract type
- Internet services
- Customer support
- Payment methods


The model predicts:

- Low churn risk
- High churn risk


SHAP explainability shows which factors influenced the prediction.


## 🛠️ Tech Stack

### Machine Learning
- Python
- Scikit-learn
- XGBoost
- SHAP

### Frontend
- Streamlit

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib
- Plotly


## 📂 Project Structure
Telecom-Churn-Prediction

│
├── app
│ └── streamlit_app.py
│
├── dashboard
│ └── dashboard.py
│
├── models
│ ├── churn_model.pkl
│ └── feature_names.pkl
│
├── reports
│ └── report_generator.py
│
├── requirements.txt
│
└── README.md



## 📊 Model Workflow

1. Customer data input
2. Data preprocessing
3. ML prediction
4. Churn probability calculation
5. SHAP explanation generation
6. Retention recommendation


## 📈 Business Value

This system helps telecom companies:

- Identify customers at risk
- Understand churn reasons
- Improve retention strategies
- Reduce customer loss


## ▶️ Run Locally


Install dependencies:
pip install -r requirements.txt


Run application:
streamlit run app/streamlit_app.py


## 👩‍💻 Author

Gopika S Nambiar