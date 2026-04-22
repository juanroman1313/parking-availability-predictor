from fastapi import APIRouter, HTTPException, Depends
from app.base import SessionLocal
from app.models.user import User
from app.models.parking_report import ParkingReport
from app.models.parking_availability_stats import ParkingAvailabilityStats
from app.models.zone import Zone
from app.schemas.parking_report_schema import ParkingReportCreate, ParkingReportResponse
from app.security import get_current_user
from app.stats_utils import calculate_probability
import datetime

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/createReport", response_model = ParkingReportResponse)
def create_report(
    report: ParkingReportCreate, 
    current_user: User = Depends(get_current_user)
    ):
    with SessionLocal() as session:
        existing_zone = session.query(Zone).filter(Zone.id == report.zone_id).first()
        if not existing_zone:
            raise HTTPException(status_code=400, detail="Zone does not exist")
        dtTrunct = report.time_slot.replace(second=0,minute=0)
        new_report = ParkingReport(
            user_id=current_user.id,
            zone_id=report.zone_id,
            time_slot=dtTrunct,
            availability=report.availability
        )
        session.add(new_report)
        session.commit()
        #Consultar si ya existe en stats una fila con zona y time slot
        existing_stat = session.query(ParkingAvailabilityStats).filter(ParkingAvailabilityStats.zone_id == report.zone_id).filter(ParkingAvailabilityStats.time_slot == dtTrunct).first()
        probability, reports = calculate_probability(session, report.zone_id, dtTrunct)
        if (existing_stat == None):
            new_parking_availability_stat = ParkingAvailabilityStats(
                zone_id = report.zone_id,
                time_slot = dtTrunct,
                probability = probability ,
                total_reports = reports
            )
            session.add(new_parking_availability_stat)
            session.commit()
            session.refresh(new_parking_availability_stat)
        else:
            existing_stat.probability = probability
            existing_stat.total_reports = reports
            existing_stat.updated_at = datetime.datetime.now(datetime.timezone.utc)
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