# Database design

## List of tables
-**Users**: Stores registered users of the system. A user represents a driver who can authenticate and submit parking reports.
-**Zones**: Represents geographical areas where parking availability is tracked. Zones are used to group parking reports and calculate availability probabilities.
-**ParkingReports**: Stores individual parking reports submitted by registered users. Each report indicates whether parking was found in a specific zone and time slot.
-**ParkingAvailabilityStats**: Stores precomputed parking availability probabilities for each zone and time slot. This table is used to improve performance when querying parking availability.

## Users Table
- id (PK,int)
- email (string)
- password_hash (string)
- created_at (datetime)

## Zones Table
- id (PK, int)
- name (string)
- latitude (float)
- longitude (float)

## ParkingReports Table
- id (PK, int)
- user_id (FK, int)
- zone_id (FK, int)
- time_slot (datetime)
- availability (Boolean)
- created_at (datetime)

## ParkingAvailabilityStats Table
- id (PK, int)
- zone_id (FK, int)
- time_slot (datetime)
- probability (float)
- updated_at (datetime)
- total_reports (int)

## Table Relationships

- A user can create many parking reports. A parking report belongs to one user.
- A zone can have many parking reports. A parking report belongs to one zone.
- ParkingAvailabilityStats belongs to one zone and is specific to one time_slot.
