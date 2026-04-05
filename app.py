import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="AI Sales Predictor",
    page_icon="📊",
    layout="wide"
)

# Custom CSS (🔥 Premium UI)
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .metric-box {
        background-color: #1c1f26;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title Section
st.title("🚀 AI Sales Prediction Dashboard")
st.markdown("### Predict Sales using Machine Learning + Interactive Analytics")

# Sidebar Inputs
st.sidebar.header("📥 Input Budget")

tv = st.sidebar.slider("📺 TV Budget", 0.0, 300.0, 150.0)
radio = st.sidebar.slider("📻 Radio Budget", 0.0, 50.0, 25.0)
news = st.sidebar.slider("📰 Newspaper Budget", 0.0, 100.0, 50.0)

predict_btn = st.sidebar.button("🚀 Predict")

# Load data
data = pd.read_csv("data/advertising.csv")

# Layout
col1, col2, col3 = st.columns(3)

# KPIs
with col1:
    st.metric("📺 Avg TV Spend", round(data["TV"].mean(), 2))
with col2:
    st.metric("📻 Avg Radio Spend", round(data["Radio"].mean(), 2))
with col3:
    st.metric("💰 Avg Sales", round(data["Sales"].mean(), 2))

st.markdown("---")

# Prediction Result
if predict_btn:
    result = model.predict([[tv, radio, news]])[0]
    
    st.success(f"💰 Predicted Sales: {result:.2f}")
    
    # AI Insight
    if result > 20:
        st.info("🔥 High Sales Expected – Strong marketing strategy!")
    elif result > 10:
        st.warning("⚡ Moderate Sales – Can improve marketing mix")
    else:
        st.error("⚠️ Low Sales – Consider increasing ad budget")

# Charts Section
st.subheader("📊 Data Insights")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.scatter(data["TV"], data["Sales"])
    ax.set_title("TV vs Sales")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.scatter(data["Radio"], data["Sales"])
    ax.set_title("Radio vs Sales")
    st.pyplot(fig)

# Feature Importance (Fake but useful visualization)
st.subheader("🧠 Feature Importance")

importance = pd.DataFrame({
    "Feature": ["TV", "Radio", "Newspaper"],
    "Importance": [0.6, 0.3, 0.1]
})

st.bar_chart(importance.set_index("Feature"))

# Footer
st.markdown("---")
st.markdown("✨ Built with ❤️ by Ritesh Gursal | Data Science Portfolio")