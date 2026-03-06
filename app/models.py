from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, func, DateTime

Base = declarative_base()

class User(Base): 
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())