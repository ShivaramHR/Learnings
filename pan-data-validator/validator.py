import pandas as pd
import re

df = pd.read_csv("data/pan-data.csv")
# print(df.head())
# print(f"Total: {len(df)}")
 
# Data cleaning
df["PAN"] = df["PAN"].astype(str).str.strip().str.upper()
df = df.dropna(subset=['PAN']).drop_duplicates(subset=['PAN'])

def is_valid_pan(pan):
    if len(pan) != 10:
        return False
    
    if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', pan):
        return False
    return True

df['Status'] = df['PAN'].apply(lambda x: 'Valid' if is_valid_pan(x) else 'Invalid')

df_summary = pd.DataFrame({ "Total": [len(df)],
                            "Valid": [df['Status'].value_counts().get('Valid', 0)], 
                            "Invalid": [df['Status'].value_counts().get('Invalid', 0)]})
df.to_csv("data/pan_validation.csv", index=False)
df_summary.to_csv("data/pan_summary.csv", index=False)
    
    