import streamlit as st
import joblib

from deploy import predict

# Cache the loading process so it doesn't reload the files every time a user clicks a button
@st.cache_resource
def load_ml_artifacts():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_ml_artifacts()

st.title("Purchase Prediction Model")
st.write("Enter the customer's details to predict if they will make a purchase.")

with st.form("prediction_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    salary = st.number_input("Estimated Salary ($)", min_value=0, step=1000, value=50000)
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    submit_button = st.form_submit_button("Predict")

if submit_button:
    gender_male = 1 if gender == "Male" else 0
    
    scaled_values = scaler.transform([[age, salary]])
    scaled_age = scaled_values[0][0]
    scaled_salary = scaled_values[0][1]
    
    
    prediction = predict(scaled_age, scaled_salary, gender_male)
    
    st.divider()
    if prediction == "Purchased":
        st.success("🎯 Prediction: **Purchased**")
    else:
        st.error("🛑 Prediction: **Not Purchased**")