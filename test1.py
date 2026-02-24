import yfinance as yf
import pandas as pd

TICKER = "TSM"
PERIOD = "2y"
INTERVAL = "1d"

df = yf.download(TICKER, period=PERIOD, interval=INTERVAL, auto_adjust=False, progress=False)

# ✅ 如果是 MultiIndex 欄位（常見形狀像 ('Close','TSM')），先把它取成單一 ticker 的表
if isinstance(df.columns, pd.MultiIndex):
    # 欄位通常是 level=0: Open/High/Low/Close... level=1: TICKER
    df = df.xs(TICKER, axis=1, level=1)

df = df.dropna()

price_col = "Close"     # 想用調整後價格就改成 "Adj Close"
close = df[price_col]   # 這裡現在一定是 Series

# 計算 MA
for n in [20, 50, 100, 200]:
    df[f"MA{n}"] = close.rolling(n).mean()

# 取最新一筆
latest_row = df.iloc[-1]
last_date = df.index[-1].date()
last_close = float(latest_row[price_col])  # ✅ 這裡會是 scalar，不會再是 Series

print(f"{TICKER}  date={last_date}  {price_col}={last_close:.2f}")
for n in [20, 50, 100, 200]:
    ma = float(latest_row[f"MA{n}"])
    diff_pct = (last_close / ma - 1) * 100
    print(f"MA{n}: {ma:.2f}  ({diff_pct:+.2f}%)")