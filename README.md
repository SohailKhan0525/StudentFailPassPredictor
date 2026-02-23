# 🎓 Student Pass/Fail Predictor

A machine learning project that predicts whether a student will **PASS** or **FAIL** based on demographic and academic background features.

---

## 📁 Project Files

| File | Description |
|---|---|
| `pass_fail_model.pkl` | Trained Logistic Regression classifier |
| `columns.pkl` | Ordered list of one-hot encoded feature columns used during training |
| `unique_categories.pkl` | Valid category values for each input feature |

---

## 🧠 What I Learned

### 1. Problem Type — Binary Classification

The target variable is binary:

- `0` → **Fail**
- `1` → **Pass**

The model outputs a **probability** for each class via `predict_proba`, and the higher-probability class is used as the prediction.

---

### 2. Input Features

Five categorical features are used as inputs:

| Feature | Categories |
|---|---|
| Gender | `female`, `male` |
| Race / Ethnicity | `group A`, `group B`, `group C`, `group D`, `group E` |
| Parental Level of Education | `associate's degree`, `bachelor's degree`, `high school`, `master's degree`, `some college`, `some high school` |
| Lunch Type | `free/reduced`, `standard` |
| Test Preparation Course | `completed`, `none` |

---

### 3. One-Hot Encoding (`pd.get_dummies`)

Since all inputs are **categorical**, they are converted to numeric binary columns using one-hot encoding with `pd.get_dummies`.  
To avoid the **dummy variable trap** (multicollinearity), one category per feature is dropped as the reference/baseline level.

The 12 encoded columns saved in `columns.pkl` are:

```
gender_male
race/ethnicity_group B
race/ethnicity_group C
race/ethnicity_group D
race/ethnicity_group E
parental level of education_bachelor's degree
parental level of education_high school
parental level of education_master's degree
parental level of education_some college
parental level of education_some high school
lunch_standard
test preparation course_none
```

> **Dropped (baseline) categories:** `gender_female`, `race/ethnicity_group A`, `parental level of education_associate's degree`, `lunch_free/reduced`, `test preparation course_completed`

When encoding new input, `df_encoded.reindex(columns=columns, fill_value=0)` ensures the column order and set exactly match training — this is critical for correct inference.

---

### 4. Model — Logistic Regression

**Algorithm:** `sklearn.linear_model.LogisticRegression`

| Hyperparameter | Value | Why |
|---|---|---|
| `penalty` | `l2` | Ridge regularization — penalizes large coefficients to reduce overfitting |
| `C` | `1.0` | Inverse regularization strength (default, balanced) |
| `solver` | `lbfgs` | Efficient quasi-Newton solver suited to small/medium datasets |
| `max_iter` | `1000` | Extended from the default 100 to allow convergence |
| `class_weight` | `balanced` | Automatically adjusts weights inversely proportional to class frequencies — handles class imbalance |
| `random_state` | `42` | Ensures reproducibility |

---

### 5. Feature Coefficients & Their Meaning

The trained model's coefficients show how each binary feature influences the **log-odds of passing** (positive = more likely to pass, negative = less likely):

| Feature | Coefficient | Interpretation |
|---|---|---|
| `lunch_standard` | +1.198 | Standard lunch is the strongest positive predictor |
| `parental level of education_master's degree` | +1.031 | Highest parental education boosts pass probability |
| `race/ethnicity_group D` | +0.965 | Positive relative to group A baseline |
| `race/ethnicity_group E` | +0.962 | Positive relative to group A baseline |
| `race/ethnicity_group C` | +0.340 | Slightly positive |
| `parental level of education_some college` | +0.271 | Mild positive effect |
| `parental level of education_bachelor's degree` | −0.094 | Near-neutral |
| `race/ethnicity_group B` | −0.165 | Slightly negative relative to group A |
| `parental level of education_high school` | −0.686 | Negative relative to associate's degree |
| `gender_male` | −0.868 | Males slightly less likely to pass relative to females in this dataset |
| `parental level of education_some high school` | −0.934 | Negative effect |
| `test preparation course_none` | −1.028 | Not completing prep course strongly lowers pass probability |

---

### 6. Model Persistence with `joblib`

`joblib.dump` / `joblib.load` is used to serialize and reload the trained model and supporting objects:

```python
import joblib

# Save
joblib.dump(model, "pass_fail_model.pkl")
joblib.dump(columns, "columns.pkl")
joblib.dump(unique_categories, "unique_categories.pkl")

# Load
model = joblib.load("pass_fail_model.pkl")
columns = joblib.load("columns.pkl")
unique_categories = joblib.load("unique_categories.pkl")
```

`joblib` is preferred over `pickle` for scikit-learn objects because it is more efficient when the object contains large NumPy arrays.

---

## ⚠️ Disclaimer

This project is for **educational and demonstration purposes only**. Predictions are based on a sample dataset and **must not** be used for real academic decisions.

---

## 📄 License

Personal learning project. Provide credit if reused.
