# Parking Availability Prediction Algorithm

## 1. Algorithm Overview
The algorithm estimates parking availability using historical user reports. Reports are grouped by zone and time slot. The probability is calculated as the ratio between reports where parking was found and the total number of reports.

## 2. Data Used
- `zone_id` – ID of the zone
- `time_slot` – Day and hour or range
- `availability` – Whether parking was found (FOUND / NOT_FOUND)

## 3. Probability Calculation
- Group reports by `zone_id` and `time_slot`
- Count total reports and number of FOUND reports
- Probability = `found_reports / total_reports`
- If there are few or no reports, the system will display "Insufficient data"

## 4. Result Visualization
- Color code:
  - Green → High probability (easy)
  - Yellow → Medium probability
  - Red → Low probability (difficult)
  - White → Insufficient data 
- Optionally show numeric probability

## 5. Storage / Calculation Strategy
Precompute and store results in a separate table to improve query performance and scalability.

## 6. Considerations & Future Improvements
- Handling low number of reports
- Optionally weigh recent reports more heavily
- Extendable to ML-based prediction in the future
