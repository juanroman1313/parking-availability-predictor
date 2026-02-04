from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.base import Base
import datetime

class ParkingReport(Base):
    __tablename__ = "parking_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    zone_id = Column(Integer, ForeignKey("zones.id"))
    time_slot = Column(DateTime, nullable=False)
    availability = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="parking_reports")
    zone = relationship("Zone", back_populates="parking_reports")
