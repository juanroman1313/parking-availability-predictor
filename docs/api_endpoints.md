# API Endpoints – Parking Availability Predictor

| Endpoint | Method | Description | Request | Response | Auth |
|----------|--------|-------------|---------|---------|------|
| /users/register | POST | Register a new user | `{ "name": "...", "email": "...", "password": "..." }` | `{ "id": 1, "name": "...", "email": "..." }` | No |
| /users/login | POST | Login | `{ "email": "...", "password": "..." }` | `{ "token": "JWT_TOKEN" }` | No |
| /users/{id} | GET | Get user profile | None | `{ "id": 1, "name": "...", "email": "..." }` | Yes |
| /zones | GET | Get all zones | None | `[ { "id": 1, "name": "Zone A", "lat": ..., "lng": ... }, ... ]` | No |
| /zones/{id}/availability | GET | Get parking probability for a zone & time | `?day=MONDAY&hour=18` | `{ "zone_id": 1, "probability": 0.25 }` | No |
| /reports | POST | Create parking report | `{ "user_id": 1, "zone_id": 2, "time_slot": "18:00-19:00", "availability": "FOUND" }` | `{ "report_id": 10, "status": "ok" }` | Yes |
| /reports | GET | List all reports (optional) | None | `[ { "id": 10, "user_id": 1, "zone_id": 2, "time_slot": "...", "availability": "FOUND" }, ... ]` | Yes |
