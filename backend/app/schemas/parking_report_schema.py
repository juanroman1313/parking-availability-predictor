from pydantic import BaseModel
from datetime import datetime
class ParkingReportCreate(BaseModel):
    zone_id: int
    time_slot: datetime
    availability: bool

class ParkingReportResponse(BaseModel):
    id: int
    zone_id: int
    availability: bool
    time_slot: datetime
    user_id: int

    class Config:
        orm_mode = True