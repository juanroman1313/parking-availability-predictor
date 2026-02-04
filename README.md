# parking-availability-predictor

## Problem
The problem addressed by this application is the lack of information available to drivers about the probability of finding parking in a specific area and time slot.

## Objective
The goal of the system is to allow users to report parking availability in a given area and time slot. Based on historical data, the system provides an estimation of how likely it is to find parking in that area.

## Use Cases
### UC-1: Register parking report
**Actor:** Registered driver  
**Description:** The driver parks in an area at a given time and reports it to the system.  
**Result:** The system stores the report.

### UC-2: Check parking availability
**Actor:** Anonymous / Registered driver  
**Description:** The driver checks parking availability in a given area.  
**Result:** The system displays a color-coded map indicating parking probability.

### UC-3: User registration
**Actor:** Anonymous user  
**Description:** The user creates an account.  
**Result:** The system registers the user.

### UC-4: User login
**Actor:** Registered user  
**Description:** The user authenticates into the system.  
**Result:** The system grants access to restricted features.

## 📄 Documentation
- [API Endpoints](docs/api_endpoints.md)
- [Backend Structure](docs/backend_structure.md)
- [Database Design](docs/database_design.md)
- [Prediction Algorithm](docs/prediction_algorithm.md)
- [Frontend Structure](docs/frontend_structure.md)
- [Domain Model](docs/domain_model.md)