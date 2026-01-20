# PROJECT TITLE: APPLE (AAPL) STOCK PRICE ANALYSIS
# AUTHOR: Module 1 - Data Analysis with Python
# DESCRIPTION:
# This program analyzes historical Apple stock prices using
# Python. It downloads data, cleans it, computes indicators,
# visualizes trends, and evaluates performance.


# IMPORT REQUIRED LIBRARIES
# pandas: used for data manipulation and analysis
# yfinance: used to fetch stock market data from Yahoo Finance
# matplotlib: used for plotting graphs
# os: used to check current working directory

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import os


# STEP 1: DOWNLOAD STOCK DATA
# We fetch Apple (AAPL) stock data for the year 2023.
# The data includes Open, High, Low, Close prices and Volume.

df = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

# STEP 2: FIX MULTI-INDEX COLUMNS
# yfinance sometimes returns columns with multiple index levels.
# This line flattens the columns so we can work with them easily.

df.columns = df.columns.get_level_values(0)

# STEP 3: INSPECT THE DATA
# We print the first 5 rows to understand the structure
# and verify that data was downloaded correctly.

print("\n--- FIRST 5 ROWS OF DATA ---")
print(df.head())

# STEP 4: SELECT RELEVANT COLUMNS
# We only keep the columns needed for analysis.
# Using .copy() avoids pandas warnings later.

prices = df[["Open", "High", "Low", "Close", "Volume"]].copy()

# STEP 5: CHECK FOR MISSING VALUES
# Missing values can break calculations.
# A value of 0 means the column is complete.

print("\n--- MISSING VALUES ---")
print(prices.isnull().sum())

# STEP 6: CALCULATE TECHNICAL INDICATORS
# Simple Moving Averages:
# - SMA 20: short-term trend
# - SMA 50: medium-term trend

prices["SMA_20"] = prices["Close"].rolling(window=20).mean()
prices["SMA_50"] = prices["Close"].rolling(window=50).mean()

# STEP 7: CALCULATE DAILY RETURNS
# Daily return shows the percentage price change from
# one trading day to the next.

prices["Daily_Return"] = prices["Close"].pct_change()

# STEP 8: VISUALIZE STOCK PRICE AND MOVING AVERAGES
# Line plots help us see price trends and indicator behavior.

print("\n--- ABOUT TO PLOT PRICE DATA ---")

plt.figure(figsize=(12, 6))

# Plot closing price
plt.plot(prices["Close"], label="Close Price")

# Plot moving averages
plt.plot(prices["SMA_20"], label="20-Day SMA")
plt.plot(prices["SMA_50"], label="50-Day SMA")

# Add labels and legend
plt.title("Apple (AAPL) Stock Price Analysis - 2023")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()

# Display the plot
plt.show()
print("\n--- FINISHED PLOTTING ---")

# STEP 9: CALCULATE CUMULATIVE RETURN
# Cumulative return shows how an investment grows over time.
# It assumes profits are reinvested.

prices["Cumulative_Return"] = (1 + prices["Daily_Return"]).cumprod()

# STEP 10: DISPLAY FINAL RESULTS
# We print the last few rows to observe final indicators
# and cumulative performance.

print("\n--- LAST 5 ROWS ---")
print(prices.tail())

# STEP 11: FINAL RETURN CALCULATION
# This represents the total gain or loss for the year.

final_return = prices["Cumulative_Return"].iloc[-1] - 1
print(f"\nFinal return: {final_return:.2%}")

# STEP 12: SAVE PROCESSED DATA
# Saving results allows further analysis or reporting.

prices.to_csv("aapl_stock_analysis.csv")

# STEP 13: CONFIRM FILE LOCATION
# This prints where the CSV file is saved.

print("\nSaved file at:", os.getcwd())

# END OF PROGRAM
# This project demonstrates:
# - Real-world data analysis
# - Financial indicators
# - Visualization techniques
# - Clean, readable Python code
