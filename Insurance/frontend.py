import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/predict"


st.title("Insurance Prediction App")
st.markdown("### Enter your details below:")

# Input Field
age = st.number_input("Enter age : ", min_value=1, max_value=120, value=30)
weight = st.number_input("Enter weight :", min_value= 1.0, value=40.0)
height = st.number_input("Enter height :", min_value=0.5,max_value=2.49, value=1.60)
income_lpa = st.number_input("Enter Income :", min_value=.1, value=2.0)
smoker = st.selectbox("Are you a smoker :", options=[False, True])
city = st.text_input("Enter city :", value="Mumbai")
occupation = st.selectbox("Enter occupation", options=['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium Category"):
  input_data = {
    "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
  }

  try:
    response = requests.post(API_URL, json=input_data)
    result = response.json()

    st.write(result)
    if response.status_code == 200 and "predicted_category" in result:
      prediction = result['predicted_category']
      st.success(f"Predicted Insurance Premium Category: {prediction}")
    else:
      st.error(f"API Error : {response.status_code}")
      st.write(result)

  except requests.exceptions.ConnectionError:
    st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")