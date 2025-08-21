from sqlalchemy import create_engine

# Database connection URL format:
# postgresql://username:password@host:port/database
DATABASE_URL = "postgresql://postgres:lavannya.vit28@localhost:5432/skillscope"

# Create an engine
engine = create_engine(DATABASE_URL)

# Test connection
try:
    with engine.connect() as connection:
        print("✅ Connected to PostgreSQL successfully!")
except Exception as e:
    print("❌ Error connecting to database:", e)
