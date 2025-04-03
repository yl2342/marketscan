# Marketscan Data Analysis Project

This repository contains tools and documentation for working with Marketscan healthcare data, including Commercial Claims and Encounters (CCAE), Medicare Supplemental (MDCR), and Medicaid data.

## Project Structure

- `ccae/`: Commercial Claims and Encounters data processing
- `mdcr/`: Medicare Supplemental data processing
- `medicaid/`: Medicaid data processing
- `provider/`: Provider-related data processing
- `NDC_directory/`: National Drug Code directory and processing
- `data_documentation/`: 
  - `User Guide/`: Documentation for data usage
  - `Data Dictionary/`: Detailed data field descriptions
- `reference/`: Reference materials and documentation

## Data Sources

### National Drug Code (NDC) Directory
- The NDC directory is used for drug identification and processing
- To keep your downloaded data up to date, you need to re-download the data every time it is updated
- [Download page (zip json file, 26mb, last updated on 2025-03-11)](https://open.fda.gov/apis/drug/ndc/download/)
- Note: NDC is typically 11 digits for insurance or Medicare purposes

## Setup

1. Create a conda environment using the provided requirements.txt:
```bash
conda create --name marketscan --file requirements.txt
```

2. Activate the environment:
```bash
conda activate marketscan
```

## Dependencies

The project uses a comprehensive set of Python packages for data analysis and processing, including:
- pandas
- numpy
- matplotlib
- pyspark
- duckdb
- and other data processing libraries

All dependencies are listed in `requirements.txt`.

## Documentation

For detailed information about the data and its usage, please refer to:
- `data_documentation/User Guide/` for usage instructions
- `data_documentation/Data Dictionary/` for field descriptions and data structure



