# scripts/update_data.py

import os

print("🚀 Running update pipeline...")

os.system("python clean_data.py")
os.system("python combine_datasets.py")

print("✅ All datasets cleaned and final_jobs.csv updated!")
