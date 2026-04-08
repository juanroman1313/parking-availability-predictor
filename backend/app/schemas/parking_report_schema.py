from pydantic import BaseModel
from datetime import datetime
class ParkingReportCreate(BaseModel):
    zone_id: int
    time_slot: datetime
    availability: bool