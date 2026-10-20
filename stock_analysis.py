import pandas as pd
import yfinance as yf

TICKERS = ["CMG", "MCD", "CAVA"]

START_DATE = "2026-06-15"
END_DATE = "2026-08-15"

raw = yf.download(
    TICKERS,
    start=START_DATE,
    end=END_DATE,
    auto_adjust=True,
    progress=False
)

print("Shape:")
print(raw.shape)
