# 🎓 Student Pass/Fail Predictor (Streamlit App)

Machine learning demo that predicts whether a student will **PASS** or **FAIL** based on demographic and education-related inputs.

🔗 **Live App:**  
[Student Pass/Fail Predictor](https://studentfailpasspredictor-hjymwbpsp4bksec9ycb2xz.streamlit.app/)

---

## ✅ What’s Included (File Analysis)

- **app.py** – Streamlit UI, model inference, and probability-based result output.
- **pass_fail_model.pkl** – Trained classifier used for predictions.
- **columns.pkl** – One-hot encoded feature order used during training.
- **unique_categories.pkl** – Valid dropdown categories for inputs.
- **requirements.txt** – Python dependencies.

---

## ✨ Features

- Interactive UI with dropdown inputs
- Pass/Fail probability display
- One-hot encoding aligned to training columns
- Safety disclaimer for educational use only

---

## ▶️ Run Locally

1. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

2. Start the app:

	```bash
	streamlit run app.py
	```

---

## 🧠 Model Inputs

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course

---

## ⚠️ Disclaimer

This app is for **educational and demonstration** purposes only. Predictions are based on a sample dataset and **must not** be used for real academic decisions.

---

## 📄 License

Personal learning project. Provide credit if reused.
