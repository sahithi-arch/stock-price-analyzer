# stock-price-analyzer
Stock price analyzer using Python for ML predictions and Java for visualization/dashboard.
# Stock Price Analyzer 📈

A stock price analysis and prediction system built using Python and Java.

## 🚀 Features
- Fetch real stock data using yfinance
- Analyze stock trends
- Predict next-day stock price using Machine Learning
- REST API using Flask
- Java client to display results

## 🧠 Tech Stack
- Python: Pandas, NumPy, scikit-learn, Flask
- Java: HTTP client

## 📂 Project Structure
stock-price-analyzer/
│
├── python-backend/
│ ├── app.py
│ ├── data_fetch.py
│ ├── train_model.py
│ ├── predict.py
│ ├── requirements.txt
│
├── java-dashboard/
│ └── src/
│ └── Main.java
│
└── README.md
## ▶️ How to Run

### Python Backend

cd python-backend
pip install -r requirements.txt
python app.py


### Java Client

cd java-dashboard/src
javac Main.java
java Main


## 🌐 API Endpoint

http://localhost:5000/predict/AAPL


## 📌 Future Improvements
- Add charts and graphs
- Use advanced ML models
- Build full UI dashboard
- Deploy online
