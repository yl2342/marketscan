# CCAE (Commercial Claims and Encounters)


## Cohort Construction Flow

1. **Initial Data Assessment**
   - Total outpatient pharmaceutical (D) records: 2,378,303,451
   - Total unique patients in pharmaceutical data: 67,176,383

2. **Semaglutide User Identification**
   - Identified semaglutide orders: 7,365,976
   - Unique patients with semaglutide orders: 722,970

3. **Enrollment Criteria Application**
   - Total enrollment records: 332,870,703
   - Total unique patients in enrollment data: 111,768,892
   - Applied continuous enrollment filter to 722,970 semaglutide users: need to have 5 full years of enrollment records
     - eg  2018,2019, 2020 (first semaglutide order year), 2021, 2022 enrollment needed for patients with first semaglutide order in 2020
     - **Final cohort with 5 full years of enrollment: 70,393 (9.74%)**

4. **Enrollment Distribution**
   - 0 years: 81,120 patients (11.22%)
   - 1 year: 107,970 patients (14.94%)
   - 2 years: 139,588 patients (19.31%)
   - 3 years: 214,848 patients (29.72%)
   - 4 years: 109,003 patients (15.08%)
   - 5 years: 70,393 patients (9.74%)
        

## Data Summary Tables

| Data Type | Total Records | Total Enrollees | Cohort Records | Cohort Patients |
|-----------|---------------|----------------|----------------|-----------------|
| Lab data (r) | 915,781,306 | 10,216,389 | 170,839* | 722,970 |
| Inpatient service (s) | 457,340,872 | 9,326,880 | 2,167,855 | 24,809 |
| Inpatient admission (i) | 14,435,204 | 9,326,880 | 54,474 | 24,809 |
| Outpatient service (o) | 6,930,282,387 | 89,709,466 | 39,794,920 | 70,374 |
| Outpatient pharmaceutical (d) | 2,378,303,451 | 67,176,383 | 24,906,065 | 70,393 |

*Selected lab records for the baseline semaglutide cohort (BP, BMI, WEIGHT, HBA1C, CHOLESTEROL)


## Table 1: Cohort Characteristics
| | | | Grouped by DIABETES_HISTORY | | | |
|---|---|---|---|---|---|---|
| | | Missing | Overall | No | Yes | P-Value |
| n | | | 70393 | 14606 | 55787 | |
| Age (years), mean (SD) | | 0 | 50.2 (8.4) | 46.0 (9.5) | 51.3 (7.8) | <0.001 |
| Sex, n (%) | Female | | 42310 (60.1) | 11571 (79.2) | 30739 (55.1) | <0.001 |
| | Male | | 28083 (39.9) | 3035 (20.8) | 25048 (44.9) | |
| First Semaglutide Brand Name, n (%) | Ozempic | | 52774 (75.0) | 8143 (55.8) | 44631 (80.0) | <0.001 |
| | RYBELSUS | | 12264 (17.4) | 2011 (13.8) | 10253 (18.4) | |
| | WEGOVY | | 5355 (7.6) | 4452 (30.5) | 903 (1.6) | |
| First Semaglutide OOP ($), mean (SD) | | 0 | 92.4 (160.0) | 120.6 (236.5) | 85.1 (132.0) | <0.001 |
| First Semaglutide Total Pay ($), mean (SD) | | 0 | 1102.8 (603.1) | 1087.4 (497.7) | 1106.9 (627.7) | <0.001 |
| Average Monthly Total Pay ($), median [Q1,Q3] | | 0 | 1176.4 [707.8,1982.8] | 876.0 [523.4,1471.5] | 1265.0 [772.5,2113.4] | <0.001 |
| Average Monthly Out-of-Pocket ($), median [Q1,Q3] | | 0 | 146.5 [85.5,228.7] | 117.0 [63.8,193.2] | 154.3 [92.2,236.2] | <0.001 |


## Expenditure outcome
- Model specification
  - 







