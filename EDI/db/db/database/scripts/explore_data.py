# scripts/explore_data.py

import pandas as pd

DATA_DIR = "../data"

files = ["companies.csv", "job_postings.csv", "job_skills.csv", 
         "skills.csv", "job_industries.csv", "salaries.csv"]

for f in files:
    print("\n===== 📂", f, "=====")
    df = pd.read_csv(f"{DATA_DIR}/{f}")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Missing values:\n", df.isnull().sum())
    print("Preview:\n", df.head())
