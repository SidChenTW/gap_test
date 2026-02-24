import yfinance as yf
import pandas as pd
import talib

# 1. 下載數據
stock = yf.Ticker("NVDA")
df = stock.history(period="1mo")

# 2. 計算技術指標 (例如 RSI)
df['RSI'] = talib.RSI(df['Close'], timeperiod=14)

# 3. 簡單分析
last_rsi = df['RSI'].iloc[-1]
if last_rsi < 30:
    print(f"AAPL RSI: {last_rsi:.2f} - 超賣，考慮買入")
elif last_rsi > 70:
    print(f"AAPL RSI: {last_rsi:.2f} - 超買，考慮賣出")
else:
    print(f"AAPL RSI: {last_rsi:.2f} - 震盪")
