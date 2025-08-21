from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from db import engine   # import engine from db.py
from datetime import date

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255))
    skills = Column(Text)
    posted_date = Column(Date)

# Create all tables if not exist
Base.metadata.create_all(engine)

# Session setup
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Example insert
def insert_sample_job():
    new_job = Job(
        title="Data Scientist",
        company="Amazon",
        skills="Python, SQL, Machine Learning",
        posted_date=date.today()
    )
    session.add(new_job)
    session.commit()
    print("✅ Job inserted")

# Example fetch
def fetch_jobs():
    jobs = session.query(Job).all()
    for job in jobs:
        print(job.id, job.title, job.company, job.skills, job.posted_date)
