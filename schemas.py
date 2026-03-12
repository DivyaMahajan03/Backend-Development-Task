from pydantic import BaseModel
from datetime import date


# -------- USER SCHEMAS --------

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str


class LoginSchema(BaseModel):
    email: str
    password: str


# -------- PROJECT SCHEMA --------

class ProjectSchema(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date
    status: str
    created_by: int


# -------- DPR SCHEMA --------

class DPRSchema(BaseModel):
    user_id: int
    date: date
    work_description: str
    weather: str
    worker_count: int