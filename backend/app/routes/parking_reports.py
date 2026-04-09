from fastapi import APIRouter, HTTPException, Depends
from app.base import SessionLocal
from app.models.user import User
from app.models.parking_report import ParkingReport
from app.schemas.parking_report_schema import ParkingReportCreate, ParkingReportResponse
from app.security import get_current_user

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/createReport")
def create_report(
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

@router.get("/my-reports", response_model=list[ParkingReportResponse])
def get_user_reports(current_user: User = Depends(get_current_user)):
    with SessionLocal() as session:
        user_reports = session.query(ParkingReport).filter(ParkingReport.user_id == current_user.id).all()
        return user_reports
    
@router.get("/stats/{zone_id}")
def get_stats(zone_id:int,current_user: User = Depends(get_current_user)):
    with SessionLocal() as session:
        total_reports = session.query(ParkingReport).filter(ParkingReport.zone_id == zone_id).count()
        available_reports = session.query(ParkingReport).filter(ParkingReport.zone_id == zone_id, ParkingReport.availability == True).count()
    if total_reports == 0:
        occupancy_rate=0
    else:
        occupancy_rate = available_reports / total_reports
    return {
        "zone_id": zone_id,
        "total_reports": total_reports,
        "available_reports": available_reports,
        "occupancy_rate": occupancy_rate
    }