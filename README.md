
# 🚀 AI Sales Prediction Dashboard

An end-to-end Data Science project that predicts product sales based on advertising budget using Machine Learning and provides an interactive dashboard using Streamlit.

---

## 📌 Project Description
This project is an AI-based Sales Prediction System that uses Machine Learning to estimate product sales based on advertising budgets across different channels like TV, Radio, and Newspaper.

The main objective of this project is to analyze how advertising investment impacts sales and to build a predictive model that helps in data-driven marketing decisions.

---

## 🧠 What I Have Done
- Collected and used a real-world advertising dataset  
- Performed data preprocessing and cleaning  
- Conducted Exploratory Data Analysis (EDA)  
- Built and trained a Random Forest Regression model  
- Evaluated model using R2 Score  
- Developed an interactive dashboard using Streamlit  
- Added visualizations and business insights  
- Prepared the project for deployment  

---

## ⚙️ How It Works
The model is trained using historical data with:

**Inputs:**
- TV advertising budget  
- Radio advertising budget  
- Newspaper advertising budget  

**Output:**
- Predicted Sales  

The Random Forest model learns patterns from data and predicts sales when new inputs are provided via the dashboard.

---

## 📊 Output
- Predicted Sales Value  
- Interactive dashboard  
- Data visualization graphs  
- Business insights (High / Medium / Low sales)  
- Feature importance  

---

## 🛠️ Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

---

## ⚙️ Setup Instructions

1. Clone Repository
```bash
git clone https://github.com/your-username/sales-prediction-ml.git
cd sales-prediction-ml

---

**📂 Folder Structure*

sales-prediction-ml/
│── data/
│   └── advertising.csv
│── app.py
│── model.py
│── model.pkl   (auto-generated after running model.py)
│── requirements.txt
│── README.md
│── .gitignore

---

2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Train Model
```bash
python model.py
```
4. Run App
```bash
streamlit run app.py
```

🌐 Live Demo
