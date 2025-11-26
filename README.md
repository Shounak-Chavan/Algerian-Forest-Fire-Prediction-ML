<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-App-green?logo=flask" />
  <img src="https://img.shields.io/github/repo-size/Shounak-Chavan/Algerian-Forest-Fire-Prediction-ML" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

# 🔥 Algerian Forest Fire — FWI Prediction System
### *(Fire Weather Index Prediction using Ridge & Lasso Regression)*

This project is a **Machine Learning–based wildfire risk prediction system** that predicts the **Fire Weather Index (FWI)** — a critical metric for assessing wildfire danger. The system processes meteorological and forest data, applies advanced regression models, and delivers predictions through an interactive **Flask** web application.

The workflow includes comprehensive data cleaning, exploratory data analysis (EDA), intelligent feature engineering, correlation-based feature selection, data scaling, multiple regression model implementations, and a professional web UI for real-time predictions.

---

## 🚀 Features
- 📊 **Cleaned & Preprocessed** Algerian Forest Fires dataset
- 🔥 **FWI Prediction** using meteorological and forest parameters
- 📉 **Multiple Models** — Ridge, Lasso, ElasticNet, and Linear Regression
- ⚙️ **Production-Ready** — StandardScaler + Model persistence with Pickle
- 🌐 **Interactive Flask UI** with Bootstrap styling
- 📂 **Clean & Modular** project structure
- 📈 **Hyperparameter Tuning** with RidgeCV, LassoCV, ElasticNetCV

---

## 🛠 Tech Stack
- **Python**
- **Flask**
- **NumPy**
- **Pandas**
- **Scikit-Learn**
- **Seaborn**
- **Matplotlib**
- **Pickle**

---

## 📁 Project Structure
```
Algerian-Forest-Fire-Prediction-ML/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── Models/
│   ├── ridge.pkl
│   └── scalar.pkl
│
├── templates/
│   └── index.html
│
└── Notebooks/
    ├── Algerian_forest_fires_dataset_UPDATED.ipynb
    ├── Cleaned_Dataset
    ├── EDA.ipynb
    └── ModelTraining.ipynb
```

---

## ▶️ How to Run Locally

### **1️⃣ Clone the Repository**
```
git clone https://github.com/Shounak-Chavan/Algerian-Forest-Fire-Prediction-ML.git
cd Algerian-Forest-Fire-Prediction-ML
```

### **2️⃣ (Optional) Create Virtual Environment**
```
python -m venv venv
```

Activate the venv:

**Windows:**
```
venv\Scripts\activate
```

**Mac/Linux:**
```
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```
python app.py
```

Then open in your browser:
```
http://127.0.0.1:5000/
```

---

## 🧠 Models Used

- **Linear Regression** — Baseline model
- **Ridge Regression** — L2 regularization to prevent overfitting
- **Lasso Regression** — L1 regularization with feature selection
- **ElasticNet Regression** — Combined L1 + L2 regularization
- **Hyperparameter Tuning** — RidgeCV, LassoCV, ElasticNetCV for optimal alpha values

---


## ⚠️ Disclaimer
This project is **for educational purposes only** and should not be used for real-world prediction without proper validation and expert review.

---

## ⭐ If you found this project useful, please ⭐ the repository!
