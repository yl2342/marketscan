# Marketscan Data Analysis Project

This repository contains tools and documentation for working with Marketscan healthcare data, including Commercial Claims and Encounters (CCAE), Medicare Supplemental (MDCR), and Medicaid data (MDCD)

## Project Structure

- `ccae/`: Commercial Claims and Encounters data processing
- `mdcr/`: Medicare Supplemental data processing
- `mdcd/`: Medicaid data processing
- `provider/`: Provider-related data processing
- `previous_work_replication/`: Replication of previous work
- `NDC_directory/`: National Drug Code directory and processing
- `data_documentation/`: 
  - `User Guide/`: Documentation for data usage
  - `Data Dictionary/`: Detailed data field descriptions
- `reference/`: Reference materials and documentation

### Other Data Sources needed

#### National Drug Code (NDC) Directory
- The NDC directory is used for drug identification and processing
- To keep your downloaded data up to date, you need to re-download the data every time it is updated
- [Download page (zip json file, 26mb, last updated on 2025-03-11)](https://open.fda.gov/apis/drug/ndc/download/)
- Note: NDC is typically 11 digits for insurance or Medicare purposes



## Documentation

For detailed information about the data and its usage, please refer to:
- `data_documentation/User Guide/` for usage instructions
- `data_documentation/Data Dictionary/` for variable descriptions and data structure



