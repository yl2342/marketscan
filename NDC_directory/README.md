# NDC Directory Extraction Tool

This tool provides functionality to standardize National Drug Code (NDC) formats and extract drug products based on generic names from the FDA NDC directory.

## Features

- Standardizes NDC codes to different formats:
  - Converts 10-digit package NDCs to 11-digit format (for insurance/claims data matching)
  - Converts product NDCs to 9-digit format
- Extracts drug products matching specified generic names
- Outputs standardized and filtered data in CSV format

## Prerequisites

- Python 3.x
- Required Python packages:
  - pandas
  - json
  - argparse

## Input Files

The tool expects a JSON file containing the NDC directory data. By default, it looks for `drug-ndc-0001-of-0001.json` in the same directory.

## Usage

```bash
python3 extract_ndc_product_by_genericname.py --generic_name <generic_name> [--input_file <input_file>]
```

### Arguments

- `--generic_name`: (Required) The generic name to filter drugs by (case insensitive)
- `--input_file`: (Optional) Path to the input NDC directory JSON file. Defaults to `drug-ndc-0001-of-0001.json`

### Examples

1. Extract all products containing 'semaglutide':
```bash
python3 extract_ndc_product_by_genericname.py --generic_name semaglutide
```

2. Extract insulin products using a custom input file:
```bash
python3 extract_ndc_product_by_genericname.py --input_file custom_ndc_data.json --generic_name insulin
```

## Output

The script creates a CSV file in the `ndc_product` directory with the following naming convention:
```
ndc_product/ndc_product_{generic_name}.csv
```

The output CSV contains the following fields:
- product_ndc
- product_ndc_9digit
- generic_name
- labeler_name
- brand_name
- active_ingredients
- marketing_start_date
- listing_expiration_date
- marketing_category
- dosage_form
- product_type
- pharm_class

## NDC Standardization Rules

### Package NDC (10-digit to 11-digit)
- Format 4-4-2: Adds leading 0 (e.g., "1234-5678-90" → "01234567890")
- Format 5-3-2: Adds 0 after first segment (e.g., "12345-678-90" → "12345067890")
- Format 5-4-1: Adds 0 before last segment (e.g., "12345-6789-0" → "12345678900")

### Product NDC (to 9-digit)
- Format 4-4: Adds leading 0 (e.g., "1234-5678" → "012345678")
- Format 5-3: Adds 0 after first segment (e.g., "12345-678" → "123450678")
- Format 5-4: No padding needed (e.g., "12345-6789" → "123456789")

## Related Files

- `FDA NDC.pdf` and `National Drug Code (NDC) Info and Guide.pdf`: Documentation about NDC formats and standards
