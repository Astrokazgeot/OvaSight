import streamlit as st
import requests

st.title("🧬 OvaSight - PCOS Detection App")


with st.form("pcos_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    bmi = st.number_input("BMI", min_value=0.0, step=0.1)
    image = st.file_uploader("Upload Ultrasound Image", type=["png", "jpg", "jpeg"])
    submitted = st.form_submit_button("Predict")

    if submitted:
        if not image:
            st.error("Please upload an image.")
        else:
            with st.spinner("Processing..."):
                files = {"file": image}
                data = {"name": name, "age": age, "bmi": bmi}
                try:
                    response = requests.post("http://127.0.0.1:8000/predict", files=files, data=data)
                    if response.status_code == 200:
                        result = response.json()
                        st.success(f"Prediction: {result['prediction']}")
                        st.info(f"Ovulation Status: {result['ovulation_status']}")
                    else:
                        st.error(f"Error: {response.json()['detail']}")
                except Exception as e:
                    st.error(f"Failed to connect to backend: {e}")
