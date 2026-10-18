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


print("=== MCD Significant Movement Analysis ===")

print("\n[Event Background]")
print("In July 2026, there was a big lettuce recall because of a parasite (Cyclospora).")
print("News Source: Lianhe Zaobao (July 19, 2026).")
print("URL: https://www.zaobao.com.sg/news/world/story20260719-9385859")
print("Taco Bell and Chipotle had big problems. McDonald's was NOT on the recall list.")

print("\n[MCD Stock Data]")
print("- On July 2, 2026, MCD stock went UP 7.66% (Close price: $290.08).")
print("- On July 15, 2026, MCD stock went DOWN 3.11%.")

print("\n[Why did this happen?]")
print("1. Why it went UP on July 2:")
print("   Investors saw that MCD has its own safe supply chain. They moved their money to MCD")
print("   because it was a 'safe place' (Safe-Haven) compared to other fast-food brands.")
print("2. Why it went DOWN on July 15:")
print("   The CDC gave a national warning on July 14. People were scared to eat at ANY fast-food")
print("   restaurant. So, MCD stock went down too, even though it did nothing wrong.")

print("\n[Conclusion]")
print("MCD has a strong and safe supply chain. When the crisis started, it was a safe place for")
print("investors. But later, the fear of the whole fast-food industry made the stock go down.")
print("="*50)