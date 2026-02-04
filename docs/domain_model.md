# Domain Model

## User
Represents: A registered driver in the system
Attributes:
- id
- name
- email
- password (hashed)
Relationships:
- A user can create multiple parking reports

## Zone
Represents: A registered area in the system
Attributes:
- id
- name
- latitude (optional)
- longitude (optional)
Relationships:
- A zone can have multiple parking reports

## Parking Report
Represents: A report created by a registered user
Attributes:
- id
- user_id
- zone_id
- time_slot
- availability (FOUND / NOT_FOUND)
Relationships:
- A parking report is linked to a zone
- A parking report is created by a user
