from datetime import datetime
from pydantic import BaseModel, EmailStr

class DebugUserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime