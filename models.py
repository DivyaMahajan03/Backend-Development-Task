from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password_hash = Column(String(255))
    role = Column(Enum("admin","manager","worker"))
    created_at = Column(TIMESTAMP, server_default=func.now())


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Enum("planned","active","completed"))
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())


class DailyReport(Base):
    __tablename__ = "daily_reports"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    work_description = Column(Text)
    weather = Column(String(50))
    worker_count = Column(Integer)