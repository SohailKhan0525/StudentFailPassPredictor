# 🎓 Student Pass/Fail Predictor

## Project Overview
This is a **machine learning-powered web application** built with Streamlit that predicts whether a student will **PASS or FAIL** based on their demographic and educational background information.

The application uses a trained machine learning model to analyze student characteristics and provide prediction probabilities for pass/fail outcomes.

## USe App
[Streamlit app](https://studentfailpasspredictor-hjymwbpsp4bksec9ycb2xz.streamlit.app/)
## Features
- 🎯 **Interactive UI** - Easy-to-use Streamlit interface
- 📊 **ML-Based Predictions** - Scikit-learn model for classification
- 📈 **Probability Scores** - Shows pass/fail probability percentages
- 🎨 **User-Friendly Design** - Clear visualization of results

## Input Parameters
The model considers the following student characteristics:
- **Gender**
- **Race/Ethnicity**
- **Parental Level of Education**
- **Lunch Type**
- **Test Preparation Course**

## Technologies Used
- **Python 3.x**
- **Streamlit** - For the web interface
- **Scikit-learn** - For machine learning model
- **Pandas** - For data manipulation
- **NumPy** - For numerical operations
- **Joblib** - For model serialization

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps to Run
1. Clone the repository:
```bash
git clone https://github.com/SohailKhan0525/StudentFailPassPredictor.git
cd StudentFailPassPredictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## Project Structure
```
StudentFailPassPredictor/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── pass_fail_model.pkl      # Trained ML model
├── columns.pkl              # Feature column names
├── unique_categories.pkl    # Categorical mappings
└── README.md                # Project documentation
```

## ⚠️ Disclaimer

**This application is for educational and demonstration purposes only.** The predictions are based on a sample dataset and **should NOT be used for real academic evaluation or decision-making.**

**Important Notes:**
- Model predictions may be inaccurate and should not be relied upon for actual academic decisions
- This is a learning project to demonstrate machine learning concepts
- Always consult with educational professionals for real academic assessments
- The model's accuracy depends on the training dataset and may not generalize to all populations

## Model Information
- The model was trained on a sample dataset
- It uses one-hot encoding for categorical variables
- Classification algorithm: Pre-trained scikit-learn classifier
- Output: Binary classification (Pass/Fail) with probability scores

## Usage Example
1. Select student demographic information from dropdown menus
2. Click the "Predict Result" button
3. View the prediction result with probability percentage

## Disclaimer Caption
"This project is a machine learning demo created for learning purposes. Model predictions may be inaccurate."

## Author
- **Sohail Khan** - [GitHub](https://github.com/sohailkhan0525)

## Related Projects
Check out other projects on [Streamlit Sharing](https://share.streamlit.io/user/sohailkhan0525)

## License
This project is provided as-is for educational purposes.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or suggestions.

---

**Last Updated:** February 2026
