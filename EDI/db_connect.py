# import psycopg2

# # Database connection details
# conn = psycopg2.connect(
#     dbname="skillscope",
#     user="postgres",
#     password="lavannya.vit28",   # 🔹 replace with your postgres password
#     host="localhost",
#     port="5432"
# )

# cur = conn.cursor()

# # Example query: fetch jobs
# cur.execute("SELECT title, company, posted_date FROM jobs;")
# rows = cur.fetchall()

# print("Job Listings:")
# for row in rows:
#     print(row)

# # Close connections
# cur.close()
# conn.close()




import psycopg2
from datetime import date
from tabulate import tabulate  # install with: pip install tabulate

# Database connection
conn = psycopg2.connect(
    dbname="skillscope",
    user="postgres",
    password="lavannya.vit28",  # <- replace with your actual password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# ---------------------------
# 1. INSERT NEW JOB LISTING
# ---------------------------
def insert_job(title, company, posting_date):
    cur.execute(
        "INSERT INTO job_listings (title, company, posting_date) VALUES (%s, %s, %s)",
        (title, company, posting_date)
    )
    conn.commit()
    print(f"✅ Inserted: {title} at {company} ({posting_date})")

# Example insertion
insert_job("AI Research Intern", "OpenAI", date.today())

# ---------------------------
# 2. FETCH AND DISPLAY JOBS
# ---------------------------
cur.execute("SELECT title, company, posting_date FROM job_listings ORDER BY posting_date DESC;")
rows = cur.fetchall()

print("\n📌 Job Listings:")
print(tabulate(rows, headers=["Title", "Company", "Posting Date"], tablefmt="fancy_grid"))

# Close connection
cur.close()
conn.close()
