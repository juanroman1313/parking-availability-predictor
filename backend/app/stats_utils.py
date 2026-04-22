from app.models.parking_report import ParkingReport



def calculate_probability(session, zone_id, time_slot):
    total_reports = session.query(ParkingReport).filter(ParkingReport.zone_id == zone_id).filter(ParkingReport.time_slot == time_slot).count()
    available_reports = session.query(ParkingReport).filter(ParkingReport.zone_id == zone_id).filter(ParkingReport.time_slot == time_slot).filter(ParkingReport.availability == True).count()
    if (total_reports == 0):
        probability=0
    else:
        probability = available_reports / total_reports
    return probability,total_reports