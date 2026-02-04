# Frontend Structure

## Frontend Stack
- React: main frontend framework
- React-Leaflet: map rendering
- Axios: HTTP requests

**Why:** Leaflet is free, easy to integrate with React, and allows coloring zones based on backend data without API costs.

---

## Project Folder Structure
```text
src/
    components/
    pages/
    services/
    hooks/
    styles/
```

---

## Principal Pages

### Home / Map View
Displays an interactive map showing the user’s location and nearby zones colored according to parking availability probability. The user can also search for other areas and select a time slot to check availability.

### Login / Register
Allows users to authenticate by entering their email and password, or create a new account to access restricted features such as submitting parking reports.

### Report Parking
Enables registered users to submit a parking report indicating whether they found parking in a specific zone and time slot.

---

## Frontend Flow ↔ Backend

### Home / Map View
- Endpoint: GET /zones/{id}/availability
- Input: zone_id, time_slot
- Output: probability, total_reports, colored zones (green / yellow / red)

### Login / Register
- Endpoint:
    - POST /users/register
    - POST /users/login
- Input: email, password
- Output: authentication token, user data

### Report Parking
- Endpoint: POST /reports
- Input: zone_id, time_slot, availability
- Output: report confirmation