import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("decision_tree_model.pkl")

st.set_page_config(page_title="Kidney Disease Predictor", layout="centered")

st.title("🩺 Chronic Kidney Disease Prediction App")
st.write("Fill in the patient details below to check for CKD risk.")

# Input fields (adjusted to common CKD features)
age = st.number_input("Age", min_value=1, max_value=100, value=45)
blood_pressure = st.number_input("Blood Pressure (mm/Hg)", min_value=50, max_value=200, value=80)
specific_gravity = st.selectbox("Specific Gravity", options=[1.005, 1.010, 1.015, 1.020, 1.025])
albumin = st.slider("Albumin Level", 0, 5, 1)
sugar = st.slider("Sugar Level", 0, 5, 0)
red_blood_cells = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pus_cell = st.selectbox("Pus Cell", ["normal", "abnormal"])
pus_cell_clumps = st.selectbox("Pus Cell Clumps", ["notpresent", "present"])
bacteria = st.selectbox("Bacteria", ["notpresent", "present"])

# Encode categorical values (simplified for demo)
rbc = 1 if red_blood_cells == "normal" else 0
pc = 1 if pus_cell == "normal" else 0
pcc = 1 if pus_cell_clumps == "present" else 0
ba = 1 if bacteria == "present" else 0

# Construct feature array (must match training features exactly)
input_data = np.array([[age, blood_pressure, specific_gravity, albumin, sugar, rbc, pc, pcc, ba]])

if st.button("🔍 Predict"):
    result = model.predict(input_data)[0]
    if result == 0:
        st.error("❌ Likely Chronic Kidney Disease detected!")
    else:
        st.success("✅ No signs of Chronic Kidney Disease.")
