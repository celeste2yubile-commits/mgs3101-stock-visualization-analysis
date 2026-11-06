# Adapted from the professor's Lecture 04 examples

import yfinance as yf
import pandas as pd

# Download MCD data
mcd = yf.download(
    "MCD",
    start="2026-06-15",
    end="2026-08-16",
    auto_adjust=True,
    progress=False
)

if mcd.empty:
    raise RuntimeError("No data downloaded.")

if isinstance(mcd.columns, pd.MultiIndex):
    mcd.columns = mcd.columns.get_level_values(0)

mcd = mcd.sort_index()

# 1. Monthly summary — Lecture 04: resample
monthly_summary = mcd.resample("ME").agg({
    "Close": "mean",
    "Volume": "mean"
})

print("\n=== MCD Monthly Summary ===")
print("Monthly average adjusted close and daily volume:")
print(monthly_summary.round(2))
print("June and August are partial months.")

# 2. Daily returns — Lecture 04: pct_change
mcd["Daily_Return_Pct"] = (
    mcd["Close"].pct_change(fill_method=None) * 100
)

# Highest and lowest daily returns — Lecture 04: idxmax/idxmin
best = mcd["Daily_Return_Pct"].idxmax()
worst = mcd["Daily_Return_Pct"].idxmin()

print("\n=== MCD Movement Candidates ===")
print("Highest daily return:", best.date(),
      round(mcd.loc[best, "Daily_Return_Pct"], 2), "%")
print("Lowest daily return:", worst.date(),
      round(mcd.loc[worst, "Daily_Return_Pct"], 2), "%")

# Research July 2 and its surrounding trading days
event = mcd.loc["2026-07-02"]
window = mcd.loc["2026-07-01":"2026-07-07"]

high = window["Close"].idxmax()
low = window["Close"].idxmin()

print("\n=== MCD July 2 Movement ===")
print("Daily return:", round(event["Daily_Return_Pct"], 2), "%")
print("Adjusted close:", round(event["Close"], 2))
print("Volume:", event["Volume"])

print("Window: July 1–7")
print("Highest adjusted close:", round(window.loc[high, "Close"], 2),
      "on", high.date())
print("Lowest adjusted close:", round(window.loc[low, "Close"], 2),
      "on", low.date())

print("\nBusiness explanation:")
print("MarketWatch reported buying in MCD and other traditional-sector")
print("stocks on July 2. Broader market buying may help explain the move.")
print("This does not prove why MCD moved or show a recall-related benefit.")

print("\nSource: MarketWatch, July 2, 2026")
print(
    "https://www.marketwatch.com/livecoverage/"
    "stock-market-today-dow-jones-s-p-500-nasdaq-key-unemployment-jobs-data-june/"
    "card/investors-stock-up-on-mcdonald-s-and-other-old-school-stocks-"
    "ahead-of-july-4-holiday-QB3dW7zWPa1ohlLkNN03"
)

# 3. MCD findings
period_return = (
    mcd["Close"].iloc[-1] / mcd["Close"].iloc[0] - 1
) * 100

recall_return = mcd.loc["2026-07-17", "Daily_Return_Pct"]

print("\n=== MCD Findings ===")
print(
    f"1. MCD changed {period_return:.2f}% across the full period. "
    "This includes influences beyond the recall."
)
print(
    f"2. MCD returned {event['Daily_Return_Pct']:.2f}% on July 2. "
    "This was before the July 17 supplier recall."
)
print(
    f"3. MCD returned {recall_return:.2f}% on July 17. "
    "Compare this with CMG and CAVA; the return alone cannot prove causation."
)

print("\nRecall timeline source: FDA")
print(
    "https://www.fda.gov/food/outbreaks-foodborne-illness/"
    "investigation-multistate-outbreak-cyclospora-illnesses-"
    "iceberg-lettuce-july-2026"
)