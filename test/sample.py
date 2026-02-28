import yfinance as yf
import pandas as pd
import talib
import numpy as np

ticker = "TSM"  # 例：TSM ADR
stock = yf.Ticker(ticker)
df = stock.history(period="2y", interval="1d")
df["SMA20"] = talib.SMA(df["Close"], 20)
df["SMA60"] = talib.SMA(df["Close"], 60)
df["RSI14"] = talib.RSI(df["Close"], 14)

# 黃金交叉：今天 SMA20 > SMA60 且 昨天 SMA20 <= SMA60
df["golden_cross"] = (df["SMA20"] > df["SMA60"]) & (df["SMA20"].shift(1) <= df["SMA60"].shift(1))

# 死亡交叉
df["death_cross"] = (df["SMA20"] < df["SMA60"]) & (df["SMA20"].shift(1) >= df["SMA60"].shift(1))

# RSI 區間訊號（你可調整門檻）
df["rsi_overbought"] = df["RSI14"] > 70
df["rsi_oversold"] = df["RSI14"] < 30
print (df)

signals = df.loc[df["golden_cross"] | df["death_cross"] | df["rsi_overbought"] | df["rsi_oversold"],
                 ["Close", "SMA20", "SMA60", "RSI14", "golden_cross", "death_cross", "rsi_overbought", "rsi_oversold"]]

print(signals.tail(10))