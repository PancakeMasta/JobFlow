from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://jobflow:jobflow@localhost:5432/jobflow_db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)