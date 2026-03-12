from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Project
from schemas import ProjectSchema

router = APIRouter()

# Create Project
@router.post("/")
def create_project(project: ProjectSchema, db: Session = Depends(get_db)):

    new_project = Project(
        name=project.name,
        description=project.description,
        start_date=project.start_date,
        end_date=project.end_date,
        status=project.status,
        created_by=project.created_by
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "message": "Project created successfully",
        "project_id": new_project.id
    }


# Get All Projects
@router.get("/")
def get_projects(db: Session = Depends(get_db)):

    projects = db.query(Project).all()

    return projects


# Get Single Project
@router.get("/{id}")
def get_project(id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


# Update Project
@router.put("/{id}")
def update_project(id: int, project: ProjectSchema, db: Session = Depends(get_db)):

    db_project = db.query(Project).filter(Project.id == id).first()

    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    db_project.name = project.name
    db_project.description = project.description
    db_project.start_date = project.start_date
    db_project.end_date = project.end_date
    db_project.status = project.status
    db_project.created_by = project.created_by

    db.commit()

    return {"message": "Project updated successfully"}


# Delete Project
@router.delete("/{id}")
def delete_project(id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully"}