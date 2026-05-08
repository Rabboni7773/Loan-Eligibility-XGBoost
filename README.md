# 🏦 Loan Approval Prediction System

An end-to-end Machine Learning web application that predicts loan eligibility with **98% accuracy**. This project leverages a fine-tuned **XGBoost** model and is served via a high-performance **FastAPI** backend with a responsive **Bootstrap** frontend.

## 🚀 Features
*   **Instant Prediction:** Real-time inference using a serialized XGBoost model.
*   **High Accuracy:** Optimized using advanced hyperparameter tuning using sklearn-optmizer.BasyianSearch on XGBClassifier.
*   **Modern UI:** Responsive frontend with dedicated success/failure landing pages.
*   **CPU Optimized:** Environment-aware backend configured for smooth performance on consumer hardware.

## 🛠️ Tech Stack
*   **Backend:** FastAPI (Python 3.12)
*   **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templates
*   **Machine Learning:** XGBoost, Scikit-Learn, NumPy, Pandas
*   **Environment:** Ubuntu 24.04 LTS, Uvicorn

## 📂 Project Structure
```text
loan-pred-app/
├── main.py                    # FastAPI Application logic
├── loan_predict_xgb_model.pkl # Trained XGBoost Model
├── templates/                 # UI Components
│   ├── index.html             # Input Form
│   ├── success.html           # Approval UI
│   └── failure.html           # Rejection UI
└── README.md                  # Project Documentation
```

## 🐳 Run with Docker

If you have Docker installed, you can skip the manual setup and run the application with a single command. I have pre-built the image and hosted it on Docker Hub.

### 1. Pull the Image
```bash
docker pull rabboni7/loan-pred-app:v1
```

### 2. Run the Container
```bash
docker run -d -p 8000:8000 rabboni7/loan-pred-app:v1\
```
### 3. Access the App
Open your browser and go to:

http://127.0.0.1:8000

