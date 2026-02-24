import yfinance as yf

df = yf.download("TSM", period="2y", interval="1d", auto_adjust=False).dropna()
close = df["Close"]

for n in [20, 50, 100, 200]:
    df[f"SMA{n}"] = close.rolling(n).mean()
    df[f"EMA{n}"] = close.ewm(span=n, adjust=False).mean()

print(df[["Close","SMA20","SMA50","SMA200","EMA20","EMA50","EMA200"]].tail(5))