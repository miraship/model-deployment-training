import streamlit as st
import requests

st.set_page_config(page_title="House Price Prediction App", page_icon="🏠")

st.title("House Price Prediction App")
st.text("Estimate the market value of a house using a trained machine learning model.")

with st.form("predicition_form"):
    st.text("Please enter the following data")

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("Area")
        bedrooms = st.number_input("No of bedrooms", step=1)
        bathrooms = st.number_input("No of bathrooms", step=1)
        furnishingstatus = st.selectbox(
            "Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"]
        )

    with col2:
        mainroad = int(st.toggle("Is on the mainroad?"))
        basement = int(st.toggle("Has a basement?"))
        guestroom = int(st.toggle("Has a guestroom?"))
        hotwaterheating = int(st.toggle("Has water heating?"))
        airconditioning = int(st.toggle("Has Air Conditioning?"))
        parking = int(st.toggle("Has parking?"))

    st.divider()
    submitButton = st.form_submit_button(
        "Predict House Price", width="stretch", type="primary"
    )

    if submitButton:
        with st.spinner("Predicting house price"):
            furnishingstatus = {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}[
                furnishingstatus
            ]

            payload = {
                "area": area,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "mainroad": mainroad,
                "basement": basement,
                "stories": 0,
                "guestroom": guestroom,
                "hotwaterheating": hotwaterheating,
                "parking": parking,
                "airconditioning": airconditioning,
                "furnishingstatus": furnishingstatus,
                "prefarea": 0,
            }

            response = requests.post("http://localhost:8000/ai/predict", json=payload)
            if response.status_code == 200 and response.json():
                st.success(f"House Price: {response.json()['house_price']}")
            else:
                st.error("Internal Server Error")
