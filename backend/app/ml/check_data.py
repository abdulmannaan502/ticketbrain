import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
data_path = ROOT / "data" / "tickets_raw.csv"

print("Loading:", data_path)

df = pd.read_csv(data_path)
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
