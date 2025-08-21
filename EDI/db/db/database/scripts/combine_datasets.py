import pandas as pd
import os

# ==== PATHS ====
DATA_DIR = "../data"
FINAL_DIR = "../final_data"
os.makedirs(FINAL_DIR, exist_ok=True)

# ==== LOAD DATASETS ====
print("Loading datasets...")
companies = pd.read_csv(f"{DATA_DIR}/companies.csv")
jobs = pd.read_csv(f"{DATA_DIR}/job_postings.csv")
job_skills = pd.read_csv(f"{DATA_DIR}/job_skills.csv")
skills = pd.read_csv(f"{DATA_DIR}/skills.csv")
job_industries = pd.read_csv(f"{DATA_DIR}/job_industries.csv")
salaries = pd.read_csv(f"{DATA_DIR}/salaries.csv")

# ==== BASIC CLEANING ====
def clean_df(df):
    df = df.drop_duplicates()
    df = df.fillna("Unknown")
    return df

companies = clean_df(companies)
jobs = clean_df(jobs)
job_skills = clean_df(job_skills)
skills = clean_df(skills)
job_industries = clean_df(job_industries)
salaries = clean_df(salaries)

# ==== MERGING ====
print("Merging datasets...")

# 1. Merge jobs with companies
merged = pd.merge(jobs, companies, on="CompanyID", how="left")

# 2. Merge job_skills + skills to get skill names
job_skills_full = pd.merge(job_skills, skills, on="SkillID", how="left")

# aggregate multiple skills into one row
skills_grouped = job_skills_full.groupby("JobID")["SkillName"].apply(lambda x: ", ".join(x)).reset_index()

merged = pd.merge(merged, skills_grouped, on="JobID", how="left")

# 3. Merge industries
merged = pd.merge(merged, job_industries, on="JobID", how="left")

# 4. Merge salaries
merged = pd.merge(merged, salaries, on="JobID", how="left")

# ==== FINAL CLEAN ====
merged = clean_df(merged)

# ==== SAVE ====
output_path = f"{FINAL_DIR}/final_jobs.csv"
merged.to_csv(output_path, index=False)
print(f"✅ Final dataset saved at: {output_path}")
print("Final shape:", merged.shape)
print("Columns:", merged.columns.tolist())
