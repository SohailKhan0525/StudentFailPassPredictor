import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("pass_fail_model.pkl")
columns = joblib.load("columns.pkl")
unique_categories = joblib.load("unique_categories.pkl")
st.warning(
    "⚠️ Disclaimer: This application is for **educational and demonstration purposes only**. "
    "The predictions are based on a sample dataset and **should NOT be used for real academic evaluation "
    "or decision-making**."
)
st.set_page_config(page_title="Student Pass / Fail Predictor")
st.write("---Checkout my other apps: [Streamlit](https://share.streamlit.io/user/sohailkhan0525) | [GitHub](https://github.com/sohailkhan0525)---")
st.title("🎓 Student Pass / Fail Prediction")
st.write("Predict whether a student will PASS or FAIL")

gender = st.selectbox("Gender", unique_categories["gender"])
race = st.selectbox("Race / Ethnicity", unique_categories["race/ethnicity"])
parent_edu = st.selectbox("Parental Level of Education", unique_categories["parental level of education"])
lunch = st.selectbox("Lunch Type", unique_categories["lunch"])
prep = st.selectbox("Test Preparation Course", unique_categories["test preparation course"])

if st.button("Predict Result"):
    input_data = {
        "gender": gender,
        "race/ethnicity": race,
        "parental level of education": parent_edu,
        "lunch": lunch,
        "test preparation course": prep
    }

    df_input = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df_input)
    df_encoded = df_encoded.reindex(columns=columns, fill_value=0)

    y_prob = model.predict_proba(df_encoded)
    fail_prob = y_prob[0][0]
    pass_prob = y_prob[0][1]

    if fail_prob >= 0.5:
        st.error(f"❌ FAIL\nFail Probability: {fail_prob:.2%}")
    else:
        st.success(f"✅ PASS\nPass Probability: {pass_prob:.2%}")

st.caption(
    "This project is a machine learning demo created for learning purposes. "
    "Model predictions may be inaccurate."
)
