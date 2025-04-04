# Provider Exploration

### CCAE 
#### Inpatient service S
- Total number of records: 457,340,872
- Total number of unique ENROLID: 9,326,880
- NPI
  - An encrypted National Provider Identifier number
  - Total number of unique NPI: 984,380
  - NPI missing rate: 53.38%
- PROVIDER ID
  - Identifier for provider of service used by the carrier Encrypted as of 2001 data
  - Total number of unique PROVIDER ID: 464,462
  - PROVIDER ID missing rate: 63.49%
- NPI and PROVIDER ID
  - Total number of distinct NPI and PROVIDER ID pair: 2,075,020
  - Percentage of NPIs with multiple PROVIDER IDs: 28.75%
  - Percentage of PROVIDER IDs with multiple NPIs: 20.24%
- STDPROV
  - STDPROV missing rate: 1.91%
  - STDPROV category distribution (inpatient service records)
    - Facility: 246,283,187
    - Admitting Physicians: 104,629,755
    - Non-admitting Physicians: 72,825,171
    - Surgeons: 12,677,127
    - Unknown: 8,725,682
    - Professionals (Non-Physician): 8,666,746
    - Agencies: 3,533,204
  - STDPROV category distribution (unique ENROLID counts):
    - Facility: 8,873,783
    - Admitting Physicians: 8,152,566
    - Non-admitting Physicians: 6,131,938
    - Professionals (Non-Physician): 2,181,781
    - Surgeons: 2,112,505
    - Unknown: 658,111
    - Agencies: 475,221
  - STDPROV category distribution (unique NPI counts):
    - Admitting Physicians: 687,510
    - Professionals (Non-Physician): 283,317
    - Non-admitting Physicians: 205,475
    - Surgeons: 146,478
    - Unknown: 139,157
    - Facility: 107,895
    - Agencies: 46,814
  - STDPROV category distribution (unique PROVIDER ID counts):
    - Admitting Physicians: 290,652
    - Non-admitting Physicians: 93,361
    - Professionals (Non-Physician): 50,767
    - Surgeons: 48,926
    - Facility: 48,901
    - Unknown: 42,332
    - Agencies: 12,817

- **Provider -  Distinct Enrolled count** 
  - Select only Admitting Physicians, Professionals (Non-Physician), Non-admitting Physicians
  - Select only records with distinct_enrolid_count [1,200]
  - NPI 
    - Providers with zero enrollees: 1083 (0.05% of total)
    - Providers with more than 200 enrollees: 12485 (0.59% of total)
    - NPI provider category I distribution
      - Admitting Physicians    1,478,321
      - Professionals (Non-Physician)     376,733
      - Non-admitting Physicians          257,354
    - NPI provider category II distribution (TOP 10)
      - 204-Internal Medicine (NEC)          217,514
      - 240-Family Practice                  142,692
      - 200-Medical Doctor - MD (NEC)        136,108
      - 825-Nurse Practitioner               106,228
      - 150-Anesthesiology                   105,963
      - 220-Emergency Medicine               105,057
      - 400-Pediatrician (NEC)                98,251
      - 320-Obstetrics & Gynecology           91,315
      - 845-Physician Assistant               89,425
      - 250-Cardiovascular Dis/Cardiology     82,632
    - Histogram of associated distinct_enrolid_count by provider category I
      ![Enrollee Distribution by Provider Category](output/npi_enrollee_distribution_by_provider_category.png)
    - Histogram of associated distinct_enrolid_count by top 9 provider category II
      ![Enrollee Distribution by Provider Category](output/npi_enrollee_distribution_by_top_provider_types.png)
  - Provider ID
    - Providers with zero enrollees: 402 (0.07% of total)
    - Providers with more than 200 enrollees: 10727 (1.76% of total)
    - Provider ID provider category I distribution
      - Admitting Physicians             423,094
      - Non-admitting Physicians         102,815
      - Professionals (Non-Physician)     71,947
    - Provider ID provider category II distribution (TOP 10)
      - 204-Internal Medicine (NEC)          67,397
      - 180-Radiology                        40,283
      - 200-Medical Doctor - MD (NEC)        38,003
      - 150-Anesthesiology                   33,473
      - 240-Family Practice                  32,708
      - 320-Obstetrics & Gynecology          30,050
      - 220-Emergency Medicine               30,046
      - 250-Cardiovascular Dis/Cardiology    28,147
      - 400-Pediatrician (NEC)               27,860
      - 845-Physician Assistant              18,390
    - Histogram of associated distinct_enrolid_count by provider category I
      ![Enrollee Distribution by Provider Category](output/provid_enrollee_distribution_by_provider_category.png)
    - Histogram of associated distinct_enrolid_count by top 9 provider category II
      ![Enrollee Distribution by Provider Category](output/provid_enrollee_distribution_by_top_provider_types.png)
    


#### Outpatient service O
- Total number of records: 6,930,282,387
- Total number of unique ENROLID: 89,709,466
- NPI
  - An encrypted National Provider Identifier number
  - Total number of unique NPI: 2,216,570
  - NPI missing rate: 53.63%
- PROVIDER ID
  - Identifier for provider of service used by the carrier Encrypted as of 2001 data
  - Total number of unique PROVIDER ID: 464,462
  - PROVIDER ID missing rate: 66.39%
- NPI and PROVIDER ID
  - Total number of distinct NPI and PROVIDER ID pair: 7,862,908
  - Percentage of NPIs with multiple PROVIDER IDs: 41.59%
  - Percentage of PROVIDER IDs with multiple NPIs: 20.83%
- STDPROV
  - STDPROV missing rate: 1.91%





#### STDPROV REFERENCE TABLE:
| Code | Description |
|------|-------------|
| . | .-Missing/Unknown |
| 1 | 001-Acute Care Hospital |
| 5 | 005-Ambulatory Surgery Centers |
| 6 | 006-Urgent Care Facility |
| 10 | 010-Birthing Center |
| 15 | 015-Treatment Center |
| 20 | 020-Mental Health/Chemical Dep NEC |
| 21 | 021-Mental Health Facilities |
| 22 | 022-Chemical Depend Treatment Ctr |
| 23 | 023-Mental Hlth/Chem Dep Day Care |
| 25 | 025-Rehabilitation Facilities |
| 30 | 030-Longterm Care (NEC) |
| 31 | 031-Extended Care Facility |
| 32 | 032-Geriatric Hospital |
| 33 | 033-Convalescent Care Facility |
| 34 | 034-Intermediate Care Facility |
| 35 | 035-Residential Treatment Center |
| 36 | 036-Continuing Care Retirement Com |
| 37 | 037-Day/Night Care Center |
| 38 | 038-Hospice Facility |
| 40 | 040-Other Facility (NEC) |
| 41 | 041-Infirmary |
| 42 | 042-Special Care Facility (NEC) |
| 100 | 100-Dentist - MD & DDS (NEC) |
| 105 | 105-Dental Specialist |
| 120 | 120-Chiropractor/DCM |
| 130 | 130-Podiatry |
| 140 | 140-Pain Mgmt/Pain Medicine |
| 145 | 145-Pediatric Anesthesiology |
| 150 | 150-Anesthesiology |
| 160 | 160-Nuclear Medicine |
| 170 | 170-Pathology |
| 175 | 175-Pediatric Pathology |
| 180 | 180-Radiology |
| 185 | 185-Pediatric Radiology |
| 200 | 200-Medical Doctor - MD (NEC) |
| 202 | 202-Osteopathic Medicine |
| 204 | 204-Internal Medicine (NEC) |
| 206 | 206-MultiSpecialty Physician Group |
| 208 | 208-Proctology |
| 210 | 210-Urology |
| 215 | 215-Dermatology |
| 220 | 220-Emergency Medicine |
| 225 | 225-Hospitalist |
| 227 | 227-Palliative Medicine |
| 230 | 230-Allergy & Immunology |
| 240 | 240-Family Practice |
| 245 | 245-Geriatric Medicine |
| 250 | 250-Cardiovascular Dis/Cardiology |
| 260 | 260-Neurology |
| 265 | 265-Critical Care Medicine |
| 270 | 270-Endocrinology & Metabolism |
| 275 | 275-Gastroenterology |
| 280 | 280-Hematology |
| 285 | 285-Infectious Disease |
| 290 | 290-Nephrology |
| 295 | 295-Pulmonary Disease |
| 300 | 300-Rheumatology |
| 320 | 320-Obstetrics & Gynecology |
| 325 | 325-Genetics |
| 330 | 330-Ophthalmology |
| 340 | 340-Otolaryngology |
| 350 | 350-Physical Medicine & Rehab |
| 355 | 355-Plastic/Maxillofacial Surgery |
| 360 | 360-Preventative Medicine |
| 365 | 365-Psychiatry |
| 380 | 380-Oncology |
| 400 | 400-Pediatrician (NEC) |
| 410 | 410-Pediatric Specialist (NEC) |
| 413 | 413-Pediatric Nephrology |
| 415 | 415-Pediatric Ophthalmology |
| 418 | 418-Pediatric Orthopaedics |
| 420 | 420-Pediatric Otolaryngology |
| 423 | 423-Pediatric Critical Care Med |
| 425 | 425-Pediatric Pulmonology |
| 428 | 428-Pediatric Emergency Medicine |
| 430 | 430-Pediatric Allergy & Immunology |
| 433 | 433-Pediatric Endocrinology |
| 435 | 435-Neonatal-Perinatal Medicine |
| 438 | 438-Pediatric Gastroenterology |
| 440 | 440-Pediatric Cardiology |
| 443 | 443-Pediatric Hematology-Oncology |
| 448 | 448-Pediatric Infectious Diseases |
| 450 | 450-Pediatric Rheumatology |
| 453 | 453-Sports Medicine (Pediatrics) |
| 455 | 455-Pediatric Urology |
| 458 | 458-Child Psychiatry |
| 460 | 460-Pediatric Medical Toxicology |
| 500 | 500-Surgeon (NEC) |
| 505 | 505-Surgical Specialist (NEC) |
| 510 | 510-Colon & Rectal Surgery |
| 520 | 520-Neurological Surgery |
| 530 | 530-Orthopaedic Surgery |
| 535 | 535-Abdominal Surgery |
| 540 | 540-Cardiovascular Surgery |
| 545 | 545-Dermatologic Surgery |
| 550 | 550-General Vascular Surgery |
| 555 | 555-Head and Neck Surgery |
| 560 | 560-Pediatric Surgery |
| 565 | 565-Surgical Critical Care |
| 570 | 570-Transplant Surgery |
| 575 | 575-Traumatic Surgery |
| 580 | 580-Cardiothoracic Surgery |
| 585 | 585-Thoracic Surgery |
| 805 | 805-Dental Technician |
| 810 | 810-Dietitian |
| 815 | 815-Medical Technician |
| 820 | 820-Midwife |
| 822 | 822-Nursing Services |
| 824 | 824-Psychiatric Nurse |
| 825 | 825-Nurse Practitioner |
| 827 | 827-Nurse Anesthetist |
| 830 | 830-Optometrist |
| 835 | 835-Optician |
| 840 | 840-Pharmacist |
| 845 | 845-Physician Assistant |
| 850 | 850-Therapy (Physical) |
| 853 | 853-Therapists (Supportive) |
| 855 | 855-Therapists (Alternative) |
| 857 | 857-Renal Dialysis Therapy |
| 860 | 860-Psychologist |
| 865 | 865-Acupuncturist |
| 870 | 870-Spiritual Healers |
| 900 | 900-Health Educator/Agency |
| 905 | 905-Transportation |
| 910 | 910-Health Resort |
| 915 | 915-Hearing Labs |
| 920 | 920-Home Health Organiz/Agency |
| 925 | 925-Imaging Center |
| 930 | 930-Laboratory |
| 935 | 935-Pharmacy |
| 940 | 940-Supply Center |
| 945 | 945-Vision Center |
| 950 | 950-Public Health Agency |
| 955 | 955-Unknown Clinic |
| 960 | 960-Case Manager |
