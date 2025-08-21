# scripts/clean_data.py

import pandas as pd
import os

DATA_DIR = "../data"
CLEAN_DIR = "../final_data"
os.makedirs(CLEAN_DIR, exist_ok=True)

def clean_and_save(file):
    df = pd.read_csv(f"{DATA_DIR}/{file}")
    df = df.drop_duplicates()
    df = df.fillna("Unknown")
    df.to_csv(f"{CLEAN_DIR}/clean_{file}", index=False)
    print(f"✅ Cleaned {file} → clean_{file}")

if __name__ == "__main__":
    files = ["companies.csv", "job_postings.csv", "job_skills.csv", 
             "skills.csv", "job_industries.csv", "salaries.csv"]
    for f in files:
        clean_and_save(f)
