# Backend Structure

## 1. Project Folder Structure

``` text
app/
  models/
    user.py
    zone.py
    parking_report.py
    parking_availability_stats.py
  schemas/
    user_schema.py
    zone_schema.py
  routes/
    users.py
    zones.py
    reports.py
  services/
    prediction_service.py
  database.py
  config.py
tests/
  test_users.py
  test_reports.py
main.py
```
---

## Endpoint Mapping to Database Tables

| Endpoint | Method | Table(s) affected | Action | Auth |
|----------|--------|-----------------|--------|------|
| /users/register | POST | Users | CREATE | No |
| /users/login | POST | Users | READ | No |
| /users/{id} | GET | Users | READ | Yes |
| /zones | GET | Zones | READ | No |
| /zones/{id}/availability | GET | ParkingAvailabilityStats | READ | No |
| /reports | POST | ParkingReports | CREATE | Yes |
| /reports | GET | ParkingReports | READ | Yes |

---

## Prediction Flow

- Endpoint: GET /zones/{id}/availability
- Input: zone_id, time_slot
- Auth: Not required (any user can query availability)
- Backend:
  1. Calls the prediction service in services/prediction_service.py
  2. Fetches probability and total_reports from ParkingAvailabilityStats
  3. If data is insufficient, returns "Insufficient data"
- Output: 
```json
{ 
  "zone_id": 1, 
  "probability": 0.75, 
  "total_reports": 12 
}
```
- Note: Only this endpoint triggers the prediction service. All other endpoints (users, reports, zones) do not affect the prediction flow directly.