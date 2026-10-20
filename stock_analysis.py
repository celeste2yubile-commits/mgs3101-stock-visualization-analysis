# Import libraries
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

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

# Create normalized price chart
normalized_prices = close_prices.div(close_prices.iloc[0]) * 100

plt.figure(figsize=(10, 6))

for ticker in normalized_prices.columns:
    plt.plot(
        normalized_prices.index,
        normalized_prices[ticker],
        label=ticker
    )

plt.title("Normalized Stock Price Comparison")
plt.xlabel("Date")
plt.ylabel("Indexed Price (Start = 100)")
plt.legend()

plt.tight_layout()

plt.savefig("charts/normalized_prices.png")

plt.close()

#create mode 100644 .DS_Store

# Create daily return distribution chart
plt.figure(figsize=(8, 5))

daily_returns.boxplot()

plt.title("Daily Return Distribution")
plt.ylabel("Daily Return (%)")

plt.tight_layout()

plt.savefig("charts/return_distribution.png")

plt.close()

# Create scatterplot for CMG and MCD daily returns

plt.figure(figsize=(8, 5))

plt.scatter(
    daily_returns["CMG"],
    daily_returns["MCD"],
    alpha=0.5
)

plt.title("CMG vs MCD Daily Returns")
plt.xlabel("CMG Daily Return (%)")
plt.ylabel("MCD Daily Return (%)")

plt.tight_layout()

plt.savefig("charts/return_relationship.png")

plt.close()