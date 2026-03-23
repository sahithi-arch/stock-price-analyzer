import yfinance as yf

def fetch_stock_data(ticker="AAPL"):
    data = yf.download(ticker, period="1y")
    data.dropna(inplace=True)
    return data
