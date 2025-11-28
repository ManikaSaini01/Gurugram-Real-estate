import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate App",
)

st.markdown("""
# 🏙️ Gurugram Real Estate Insights  
### **Price Prediction & Apartment Recommendation Platform**

Welcome to the **Gurugram Real Estate Intelligence App** — an end-to-end data science project that helps users explore, evaluate, and compare apartments across the city using machine learning and smart recommendations.

---

## 🔮 Price Prediction Engine
Predict the **fair market price** of any apartment in Gurugram using models trained on real listings.  
Our ML pipeline analyzes:

- 📍 Location & sector  
- 📐 Built-up area  
- 🛏️ Bedrooms & bathrooms  
- 🏢 Property type  
- 🏘️ Amenities 

The model delivers **accurate & explainable** predictions to support informed decision-making.

---

## 🏢 Smart Apartment Recommender
Discover similar apartments instantly.  
Using a **cosine-similarity–based recommendation system**, the app matches properties by:

- 📍 Famous Location
- 🌟 Radius 
- 🏢 Nearby Appartments   

Perfect for users who want quick alternatives or more options within the same segment.

---

## 🛠️ How the Project Was Built
This app integrates the full data science lifecycle:

- 🧹 Data cleaning & preprocessing  
- 🔍 Exploratory Data Analysis (EDA)  
- 🤖 Machine learning model development  
- 🧮 Feature engineering  
- 📊 Similarity-based recommender system  
- 🚀 Deployment using **Streamlit**

---

## 🎯 Goal of the Application
To provide an intuitive, interactive platform that uses **real data + smart ML models** to simplify home-buying decisions in Gurugram.

Explore the market with clarity, confidence, and convenience.  
""")