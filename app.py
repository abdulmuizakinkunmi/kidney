import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("decision_tree_model.pkl")

st.set_page_config(page_title="CKD Predictor", layout="centered")
st.title("🩺 Chronic Kidney Disease Prediction")
st.write("Fill in the patient medical info to predict risk of CKD.")

# Numerical Inputs
age = st.number_input("Age", 1, 120, 45)
blood_pressure = st.number_input("Blood Pressure (mm/Hg)", 40, 200, 80)
specific_gravity = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
albumin = st.slider("Albumin Level", 0, 5, 1)
sugar = st.slider("Sugar Level", 0, 5, 0)
blood_glucose_random = st.number_input("Blood Glucose Random (mg/dL)", 40, 500, 120)
blood_urea = st.number_input("Blood Urea (mg/dL)", 0.0, 400.0, 50.0)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", 0.0, 50.0, 1.2)
sodium = st.number_input("Sodium (mEq/L)", 100.0, 200.0, 140.0)
potassium = st.number_input("Potassium (mEq/L)", 2.0, 10.0, 4.5)
haemoglobin = st.number_input("Hemoglobin (g/dL)", 3.0, 20.0, 12.0)
packed_cell_volume = st.number_input("Packed Cell Volume", 15, 55, 40)
white_blood_cell_count = st.number_input("WBC Count (cells/cu mm)", 3000, 18000, 7500)
red_blood_cell_count = st.number_input("RBC Count (millions/cu mm)", 2.0, 6.5, 4.8)

# Categorical Inputs
rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["notpresent", "present"])
ba = st.selectbox("Bacteria", ["notpresent", "present"])
htn = st.selectbox("Hypertension", ["no", "yes"])
dm = st.selectbox("Diabetes Mellitus", ["no", "yes"])
cad = st.selectbox("Coronary Artery Disease", ["no", "yes"])
appetite = st.selectbox("Appetite", ["good", "poor"])
ped = st.selectbox("Pedal Edema", ["no", "yes"])
anemia = st.selectbox("Anemia", ["no", "yes"])

# Encode categoricals
rbc = 1 if rbc == "normal" else 0
pc = 1 if pc == "normal" else 0
pcc = 1 if pcc == "present" else 0
ba = 1 if ba == "present" else 0
htn = 1 if htn == "yes" else 0
dm = 1 if dm == "yes" else 0
cad = 1 if cad == "yes" else 0
appetite = 1 if appetite == "good" else 0
ped = 1 if ped == "yes" else 0
anemia = 1 if anemia == "yes" else 0

# Feature vector
input_data = np.array([[
    age, blood_pressure, specific_gravity, albumin, sugar, rbc, pc,
    pcc, ba, blood_glucose_random, blood_urea, serum_creatinine, sodium,
    potassium, haemoglobin, packed_cell_volume, white_blood_cell_count,
    red_blood_cell_count, htn, dm, cad, appetite, ped, anemia
]])

# Predict button
if st.button("🔍 Predict CKD"):
    result = model.predict(input_data)[0]
    if result == 0:
        st.error("⚠️ Likely Chronic Kidney Disease detected!")
    else:
        st.success("✅ No signs of Chronic Kidney Disease.")
