from fastapi import APIRouter, HTTPException, Depends
from app.base import SessionLocal
from app.models.user import User
from app.models.parking_report import ParkingReport
from app.schemas.parking_report_schema import ParkingReportCreate
from app.security import get_current_user

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/createReport")
def createReport(
    report: ParkingReportCreate, 
    current_user: User = Depends(get_current_user)
    ):
    new_report = ParkingReport(
        user_id=current_user.id,
        zone_id=report.zone_id,
        time_slot=report.time_slot,
        availability=report.availability
    )
    with SessionLocal() as session:
        session.add(new_report)
        session.commit()
        session.refresh(new_report)
    return new_report
