from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.base import Base
import datetime

class ParkingAvailabilityStats(Base):
    __tablename__ = "parking_availability_stats"

    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(Integer, ForeignKey("zones.id"))
    time_slot = Column(DateTime, nullable=False)
    probability = Column(Float, nullable=False)
    total_reports = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    zone = relationship("Zone", back_populates="availability_stats")
