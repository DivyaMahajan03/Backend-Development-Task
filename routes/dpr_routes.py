from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import DailyReport, Project
from schemas import DPRSchema

router = APIRouter()

# Create Daily Progress Report
@router.post("/{id}/dpr")
def create_dpr(id: int, dpr: DPRSchema, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    new_report = DailyReport(
        project_id=id,
        user_id=dpr.user_id,
        date=dpr.date,
        work_description=dpr.work_description,
        weather=dpr.weather,
        worker_count=dpr.worker_count
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return {
        "message": "DPR created successfully",
        "dpr_id": new_report.id
    }


# Get DPRs for a Project
@router.get("/{id}/dpr")
def get_dpr(id: int, db: Session = Depends(get_db)):

    reports = db.query(DailyReport).filter(DailyReport.project_id == id).all()

    if not reports:
        return {"message": "No DPRs found for this project"}

    return reports