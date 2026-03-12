from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, LoginSchema
from auth import create_token
from passlib.context import CryptContext

router = APIRouter()

@router.get("/test")
def test_db(db: Session = Depends(get_db)):
    return {"message": "Database connected"}

@router.post("/register")
def register():
    return {"message": "User created"}

@router.post("/login")
def login():
    return {"token": "example_token"}