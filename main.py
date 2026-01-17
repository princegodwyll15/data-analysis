import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import os

# 1. Download Apple stock data
df = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

# Remove multi-index columns (important)
df.columns = df.columns.get_level_values(0)

print("\n--- FIRST 5 ROWS OF DATA ---")
print(df.head())

# 2. Select useful columns
prices = df[["Open", "High", "Low", "Close", "Volume"]].copy()

print("\n--- MISSING VALUES ---")
print(prices.isnull().sum())

# 3. Add indicators
prices["SMA_20"] = prices["Close"].rolling(20).mean()
prices["SMA_50"] = prices["Close"].rolling(50).mean()

# Daily percentage change
prices["Daily_Return"] = prices["Close"].pct_change()

#plotting starts here
print("\n--- ABOUT TO PLOT PRICE DATA ---")

# 4. Plot price & averages
plt.figure(figsize=(12, 6))
plt.plot(prices["Close"], label="Close Price")
plt.plot(prices["SMA_20"], label="20-Day SMA")
plt.plot(prices["SMA_50"], label="50-Day SMA")
plt.title("Apple (AAPL) Stock Price 2023")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.show()

#plotting ends here
print("\n--- FINISHED PLOTTING ---")

# 5. Cumulative return (IMPORTANT)
prices["Cumulative_Return"] = (1 + prices["Daily_Return"]).cumprod()

print("\n--- LAST 5 ROWS ---")
print(prices.tail())

# 6. Final return
final_return = prices["Cumulative_Return"].iloc[-1] - 1
print(f"\nFinal return: {final_return:.2%}")

prices.to_csv("aapl_stock_analysis.csv")
print("\nSaved file at:", os.getcwd())