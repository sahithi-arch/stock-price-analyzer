Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask, jsonify
... from data_fetch import fetch_stock_data
... from train_model import train_model
... from predict import predict_next_price
... 
... app = Flask(__name__)
... 
... @app.route("/predict/<ticker>")
... def predict(ticker):
...     data = fetch_stock_data(ticker)
...     model = train_model(data)
...     prediction = predict_next_price(model, data)
... 
...     result = {
...         "ticker": ticker,
...         "predicted_price": round(prediction, 2)
...     }
... 
...     return jsonify(result)
... 
... if __name__ == "__main__":
...     app.run(debug=True)
>>> [DEBUG ON]
>>> [DEBUG OFF]
