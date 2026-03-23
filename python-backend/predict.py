def predict_next_price(model, data):
    last_close = data[['Close']].tail(1)
    prediction = model.predict(last_close)
    return float(prediction[0])
