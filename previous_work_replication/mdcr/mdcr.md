# MDCR

## Overview

This is a collection of scripts, interim data, and results for using the MDCR data

## Cohort Construction Flow

1. **Initial Data Assessment**
   - Total outpatient pharmaceutical (D) records: 533,137,777
   - Total unique patients in pharmaceutical data: 4,963,073

2. **Semaglutide User Identification**
   - Identified semaglutide orders: 633,995
   - Unique patients with semaglutide orders: 70,591

3. **Enrollment Criteria Application**
   - Total enrollment records: 22,650,837
   - Total unique patients in enrollment data: 6,481,621
   - Applied continuous enrollment filter to 70,464 semaglutide users: need to have 5 full years of enrollment records
     - eg  2018,2019, 2020 (first semaglutide order year), 2021, 2022 enrollment needed for patients with first semaglutide order in 2020
     - **Final cohort with 5 full years of enrollment: 5,814 (8.25%)**

4. **Enrollment Distribution**
   - 0 years: 8,258 patients (11.72%)
   - 1 year: 10,141 patients (14.39%)
   - 2 years: 18,079 patients (25.66%)
   - 3 years: 18,583 patients (26.37%)
   - 4 years: 9,589 patients (13.61%)
   - 5 years: 5,814 patients (8.25%)
        

## Data Summary Tables

| Data Type | Total Records | Total Enrollees | Cohort Records | Cohort Patients |
|-----------|---------------|----------------|----------------|-----------------|
| Lab data (r) | 266,233,174 | 1,038,823 | 29,258* | 1,833 |
| Inpatient service (s) | 158,766,848 | 1,816,692 | 365,734 | 3,280 |
| Inpatient admission (i) | 3,959,288 | 1,816,691 | 9,652 | 3,280 |
| Outpatient service (o) | 1,274,602,087 | 6,051,468 | 4,705,885 | 5,813 |
| Outpatient pharmaceutical (d) | 533,137,777 | 4,963,073 | 24,906,065 | 5,814 |

*Selected lab records for the baseline semaglutide cohort (BP, BMI, WEIGHT, HBA1C, CHOLESTEROL)
