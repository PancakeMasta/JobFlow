from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse

from fastapi import APIRouter, Depends, HTTPException
from pwdlib import PasswordHash
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

router = APIRouter()

pwd_hash = PasswordHash.recommended()

@router.post("/users", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
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