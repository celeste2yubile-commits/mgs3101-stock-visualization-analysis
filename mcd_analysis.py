import yfinance as yf
import pandas as pd

print("Downloading MCD data...")
mcd = yf.download("MCD", start="2026-06-15", end="2026-08-15")

print(f"Data shape: {mcd.shape}")
print(f"Date range: {mcd.index.min()} to {mcd.index.max()}")