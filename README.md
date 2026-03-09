# 🍷 AI Wine Type Classifier

A machine learning web application that predicts whether a wine sample is **Red** or **White** based on its chemical composition.

The project demonstrates a complete ML workflow — from model training to deployment — using a FastAPI backend and a React-based user interface.

---

## 🚀 Application Overview

Users enter chemical attributes of a wine sample through the web interface.  
The system processes the input and returns:

- predicted wine type (Red or White)
- probability confidence
- visual comparison of prediction probabilities

---

## 🧠 Problem

Wine classification traditionally requires laboratory analysis and expert evaluation.  
This project shows how machine learning models can learn patterns in chemical attributes and perform automated classification.

---

## 🏗️ System Architecture

```
User Input → React UI → FastAPI API → ML Model → Prediction → UI Visualization
```

The backend handles inference while the frontend provides an interactive interface for data entry and result visualization.

---

## ⚙️ Tech Stack

### Frontend
- React (Vite)
- Axios
- Interactive form interface
- Responsive layout

### Backend
- FastAPI
- Pydantic
- Scikit-learn
- TensorFlow / Keras

### Machine Learning
- Binary classification model
- StandardScaler for feature normalization
- Wine chemistry dataset

---

## 📊 Model Features

The model uses **11 chemical properties** commonly measured in wine chemistry:

- Fixed acidity  
- Volatile acidity  
- Citric acid  
- Residual sugar  
- Chlorides  
- Free sulfur dioxide  
- Total sulfur dioxide  
- Density  
- pH  
- Sulphates  
- Alcohol  

These features allow the model to learn the chemical patterns that differentiate red and white wines.

---

## 🧾 Prediction Output

Example result:

```
Prediction: White Wine
Confidence: 78% White | 22% Red
```

The UI also visualizes the probability distribution between the two classes.

---

## 🧪 Machine Learning Pipeline

1. Dataset ingestion  
2. Data preprocessing  
3. Feature scaling (StandardScaler)  
4. Model training  
5. Model export (`.keras`)  
6. API integration for inference  
7. Frontend visualization of predictions

---

## 📁 Project Structure

```
wine-classifier/
│
├── backend/
│   ├── app/
│   ├── train/
│   ├── models/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── README.md
```

---

## 🛠️ Running the Project

### 1️⃣ Start Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

---

### 2️⃣ Start Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🧠 Training the Model

To retrain the classifier:

```bash
cd backend
python train/train_model.py
```

This generates:

- trained model
- scaler object
- feature configuration

---

## 📌 Project Highlights

- End-to-end ML application
- Clean separation of frontend and backend
- API-based model inference
- Interactive prediction interface
- Modular training pipeline

---

## 👨‍💻 Author

Vinayak Pattar  
Engineering student interested in machine learning systems and backend application development.
