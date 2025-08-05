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
![Pipeline](https://github.com/itbindu/AbiBus-Prediction/blob/main/Images/Pipe_line.jpg)
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
Evaluation results include MAE, RMSE, and R² to verify model performance.

---

## 🌐 Postman API Demo
Used **Postman** to test the deployed API:
- Send `POST` requests with bus features
- Receive the **predicted price** in the response

---

## 📡 API Usage (with Postman)

**Endpoint:**  
POST /predict



**Request Body (JSON):**
```json
{
  "bus_type": "AC",
  "seat_type": "Sleeper",
  "departure_time": "22:00",
  "duration": "9:30",
  "rating": 4.2,
  "available_seats": 12,
  "is_weekend": true,
  "days_until_travel": 3
}

Response (JSON):


{
  "predicted_price": 1250.75
}


---


