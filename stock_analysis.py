# Import libraries
import pandas as pd
import yfinance as yf

# Stock tickers
TICKERS = ["CMG", "MCD", "CAVA"]

# Analysis period
START_DATE = "2026-06-15"
END_DATE = "2026-08-15"

# Download stock data
raw = yf.download(
    TICKERS,
    start=START_DATE,
    end=END_DATE,
    auto_adjust=True,
    progress=False
)

# Display dataset information
print("Shape:")
print(raw.shape)

print("\nColumns:")
print(raw.columns)

print("\nData Types:")
print(raw.dtypes)

print("\nMissing Values:")
print(raw.isna().sum())

# Select closing prices
close_prices = raw["Close"]

print("\nClosing Prices:")
print(close_prices.head())

# Calculate daily percentage returns
daily_returns = close_prices.pct_change() * 100

print("\nDaily Returns:")
print(daily_returns.head())

# Calculate descriptive statistics for closing prices
print("\nClosing Price Statistics:")

for ticker in close_prices.columns:
    print(f"\n{ticker}")
    print("Count:", close_prices[ticker].count())
    print("Mean:", close_prices[ticker].mean())
    print("Median:", close_prices[ticker].median())
    print("Min:", close_prices[ticker].min())
    print("Max:", close_prices[ticker].max())
    print("Std:", close_prices[ticker].std())

# Calculate descriptive statistics for daily returns
print("\nDaily Return Statistics:")

for ticker in daily_returns.columns:
    print(f"\n{ticker}")
    print("Count:", daily_returns[ticker].count())
    print("Mean:", daily_returns[ticker].mean())
    print("Median:", daily_returns[ticker].median())
    print("Min:", daily_returns[ticker].min())
    print("Max:", daily_returns[ticker].max())
    print("Std:", daily_returns[ticker].std())

# Create correlation matrix
print("\nCorrelation Matrix:")

correlation_matrix = daily_returns.corr()

print(correlation_matrix)

# Create monthly average closing price summary
monthly_summary = close_prices.resample("ME").mean()

print("\nMonthly Average Closing Prices:")
print(monthly_summary)

# Save output files
monthly_summary.to_csv("outputs/monthly_summary.csv")
correlation_matrix.to_csv("outputs/correlation_matrix.csv")