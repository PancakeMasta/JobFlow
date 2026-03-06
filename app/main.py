from app.database import engine, get_db
from app.models import Base, User

from fastapi import Depends, FastAPI, HTTPException
from pwdlib import PasswordHash
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

pwd_hash = PasswordHash.recommended()

class DebugUserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

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
    
@app.post("/debug/users")
def create_test_user(payload: DebugUserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_hash.hash(payload.password)

    test_user = User(
        email=payload.email,
        hashed_password=hashed_password
    )
    
    db.add(test_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already exists")
    
    db.refresh(test_user)
    return {
        "id": test_user.id, 
        "email": test_user.email, 
        "created_at": test_user.created_at
    }