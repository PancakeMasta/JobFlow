from app.database import engine, get_db
from app.models import Base
from app.routers import users

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

app = FastAPI()
app.include_router(users.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "JobFlow API running"}

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    try:
            db.execute(text("SELECT 1"))
            return {"db": "is ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {e}")
    
