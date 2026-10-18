import yfinance as yf
import pandas as pd

print("Downloading MCD data...")
mcd = yf.download("MCD", start="2026-06-15", end="2026-08-15")

print(f"Data shape: {mcd.shape}")
print(f"Date range: {mcd.index.min()} to {mcd.index.max()}")

if isinstance(mcd.columns, pd.MultiIndex):
    mcd.columns = mcd.columns.get_level_values(0)

mcd.index = pd.to_datetime(mcd.index)
monthly_summary = mcd.resample('ME').agg({'Close': 'mean', 'Volume': 'sum'})
print("\n=== MCD Monthly Summary (June - Aug 2026) ===")
print(monthly_summary)