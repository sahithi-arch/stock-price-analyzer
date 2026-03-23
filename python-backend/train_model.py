from sklearn.linear_model import LinearRegression

def train_model(data):
    data['Prediction'] = data['Close'].shift(-1)

    X = data[['Close']][:-1]
    y = data['Prediction'][:-1]

    model = LinearRegression()
    model.fit(X, y)

    return model
