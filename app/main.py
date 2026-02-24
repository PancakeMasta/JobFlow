from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message": "JobFlow API running"}

@app.get("/health/db")
def health_db():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            return {"db": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {e}")
    