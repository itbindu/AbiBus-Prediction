# 🚌 AbhiBus Price Prediction

## 🧠 Overview
This project uses Machine Learning to predict bus ticket prices from the AbhiBus platform based on various travel features such as departure time, seat type, bus type (AC/NON-AC), and more.

---

## 📌 Problem Statement
People often struggle to estimate the right time to book bus tickets. Our system predicts bus ticket prices using real-time scraped data from AbhiBus and helps users make better booking decisions.

---

## 📊 Dataset
**Source**: Web scraped from [AbhiBus](https://www.abhibus.com/)

**Features include:**
- Bus Type (AC/Non-AC)
- Seat Type (Sleeper/Seater)
- Departure Time
- Duration
- Ratings
- Available Seats
- Price
- Weekend/Holiday Indicator

---

## ⚙️ Pipeline

- ✅ Data Collection (using Selenium & BeautifulSoup)
- ✅ Data Cleaning
- ✅ Feature Engineering
- ✅ Model Training
- ✅ Evaluation
- ✅ Prediction API with Postman
![Pipeline](images/pipeline.jpg)
---

## 🧪 Feature Engineering

- Converted date & time to numerical format
- Label encoded bus types
- Created new features: day difference, holiday flag, etc.

---

## 🤖 Model

- **Algorithm**: Decision Forest Regression
- **Metrics**: MAE, RMSE, R² Score

---

## ✅ Evaluation
*Coming soon...*

---

## 🌐 Postman API Demo

Tested the deployed API using **Postman**:

- POST requests with bus features
- Returns predicted price

---

## 📦 Requirements

Create a `requirements.txt` file with the following:

```txt
pandas
numpy
xgboost
scikit-learn
flask
selenium
beautifulsoup4
