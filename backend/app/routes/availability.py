from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from app.base import SessionLocal
from app.models.parking_availability_stats import ParkingAvailabilityStats
from sqlalchemy import func


router = APIRouter(prefix="/availability", tags=["Availability"])

@router.get("/{zone_id}")
def get_availability(
    zone_id: int,
    time_slot: datetime = Query(..., description="Franja horaria a consultar (ISO 8601)")
):
    dtTrunct = time_slot.replace(second=0,minute=0)
    with SessionLocal() as session:
        # Busca el registro con time_slot más cercano al solicitado
        stat = (
            session.query(ParkingAvailabilityStats)
            .filter(ParkingAvailabilityStats.zone_id == zone_id)
            .filter(ParkingAvailabilityStats.time_slot == dtTrunct)
            .first()
        )

        if not stat:
            raise HTTPException(
                status_code=404,
                detail=f"No hay datos de disponibilidad para la zona {zone_id}"
            )

        return {
            "zone_id": zone_id,
            "time_slot": stat.time_slot,
            "probability": stat.probability,       # 0.0 → 1.0
            "total_reports": stat.total_reports,
            "updated_at": stat.updated_at,
        }