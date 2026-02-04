from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from app.base import Base
import datetime

class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    parking_reports = relationship("ParkingReport", back_populates="zone")
    availability_stats = relationship("ParkingAvailabilityStats", back_populates="zone")
