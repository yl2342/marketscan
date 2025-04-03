#!/usr/bin/env python3
"""
This script performs two main functions:
1. Standardizes NDC (National Drug Code) formats:
   - Converts 10-digit package NDCs to 11-digit format for insurance/claims data matching
   - Converts product NDCs to 9-digit format
2. Extracts products matching a specified generic name

Example usage:
    # Extract all products containing 'semaglutide' using default input file
    python3 extract_ndc_product_by_genericname.py --generic_name semaglutide

Output:
    The script will create a CSV file with the extracted products at:
    ndc_product/ndc_product_{generic_name}.csv

"""

import json
import pandas as pd
import argparse
import os
from collections import Counter


def standardize_10digit_package_ndc_to_11digit(package_ndc_10digit):
    """
    standardize a 10-digit NDC code to an 11-digit NDC code according to the formatting rules of marketscan data (claims data)
    
    Args:
        package_ndc_10digit (str): A 10-digit NDC code in the format "XXXX-XXXX-XX", "XXXXX-XXX-XX", or "XXXXX-XXXX-X"
    
    Returns:
        str: The standardized 11-digit packageNDC code
    """
    # Remove hyphens if present
    ndc_clean = package_ndc_10digit.replace('-', '')
    
    # Check if not 10 digits, pass and print a warning
    if len(ndc_clean) != 10:
        print(f"Warning: {package_ndc_10digit} is not a 10-digit NDC code")
        return None
    
    # Determine the format by checking the original format with hyphens
    segments = package_ndc_10digit.split('-')
    if len(segments) != 3:
        print(f"Warning: {package_ndc_10digit} is not a 10-digit NDC code")
        return None
    
    segment_lengths = [len(segment) for segment in segments]
    
    # Format 4-4-2
    if segment_lengths == [4, 4, 2]:
        return f"0{segments[0]}{segments[1]}{segments[2]}"
    # Format 5-3-2
    elif segment_lengths == [5, 3, 2]:
        return f"{segments[0]}0{segments[1]}{segments[2]}"
    # Format 5-4-1
    elif segment_lengths == [5, 4, 1]:
        return f"{segments[0]}{segments[1]}0{segments[2]}"
    else:
        print(f"Warning: {package_ndc_10digit} is not in a recognized format")
        return None


def standardize_product_ndc_to_9digit(product_ndc):
    """
    standardize a 10-digit NDC code to a 9-digit NDC code according to the formatting rules of marketscan data (claims data)
    
    Args:
        product_ndc (str): A 8 or 9 digit NDC code in the format "XXXX-XXXX","XXXXX-XXX" or "XXXXX-XXXXX"
    
    Returns:
        str: The standardized 9-digit product NDC code
    """
    # Remove hyphens if present
    ndc_clean = product_ndc.replace('-', '')
    segments = product_ndc.split('-')
    
    # check if input is 8 or 9 digits and in recognized format
    if len(ndc_clean) not in [8, 9] or len(segments) != 2:
        print(f"Warning: {product_ndc} is not a 8 or 9 digit product NDC code")
        return None    
    # if 8 digits, add a leading 0
    else:
        segment_lengths = [len(segment) for segment in segments]
        # Format 4-4
        if segment_lengths == [4, 4]:
            return f"0{segments[0]}{segments[1]}"
        # Format 5-3
        elif segment_lengths == [5, 3]:
            return f"{segments[0]}0{segments[1]}"
        # Format 5-4
        elif segment_lengths == [5, 4]:
            return f"{segments[0]}{segments[1]}"
        else:
            print(f"Warning: {product_ndc} is not in a recognized format")
            return None


def main():
    """
    Main function to process arguments and execute the NDC standardization and extraction workflow.
    
    The function performs the following steps:
    1. Parse command line arguments
    2. Load the NDC directory from the specified JSON file
    3. Standardize NDC codes in memory (10-digit to 11-digit for package NDCs, etc.)
    4. Filter products by the specified generic name
    5. Extract relevant features from the matching products
    6. Save the results to a CSV file
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Standardize NDC codes and extract products by generic name',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract all semaglutide products
  python3 %(prog)s --generic_name semaglutide
  
  # Extract insulin products using a custom input file
  python3 %(prog)s --input_file custom_ndc_data.json --generic_name insulin
        """
    )
    parser.add_argument('--input_file', type=str, default='drug-ndc-0001-of-0001.json', 
                        help='Input NDC directory JSON file (default: drug-ndc-0001-of-0001.json)')
    parser.add_argument('--generic_name', type=str, required=True, 
                        help='Generic name to filter drugs by (case insensitive)')
    args = parser.parse_args()

    # Step 1: Load and standardize NDC directory
    print(f"Loading NDC directory from {args.input_file}...")
    try:
        with open(args.input_file, 'r') as f:
            ndc_directory = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Input file '{args.input_file}' is not a valid JSON file.")
        return
        
    # Validate the structure of the JSON file
    if 'results' not in ndc_directory:
        print(f"Error: Input file '{args.input_file}' does not have the expected structure (missing 'results' key).")
        return
        
    # Add standardized NDC codes
    print("Standardizing NDC codes...")
    standardized_count = 0
    error_count = 0
    
    for product in ndc_directory['results']:
        product_ndc_9digit = standardize_product_ndc_to_9digit(product['product_ndc'])
        if product_ndc_9digit:
            product['product_ndc_9digit'] = product_ndc_9digit
            standardized_count += 1
        else:
            error_count += 1
            
        for package in product.get('packaging', []):
            package_ndc_11digit = standardize_10digit_package_ndc_to_11digit(package['package_ndc'])
            if package_ndc_11digit:
                package['package_ndc_11digit'] = package_ndc_11digit
                standardized_count += 1
            else:
                error_count += 1
    
    print(f"Standardization complete: {standardized_count} NDC codes standardized, {error_count} errors.")

    # Step 2: Extract products by generic name
    print(f"Extracting products containing '{args.generic_name}'...")
    
    # Filter drugs by generic name
    filtered_drugs = [drug for drug in ndc_directory['results'] 
                     if drug.get('generic_name') and args.generic_name.lower() in drug['generic_name'].lower()]

    print(f"Found {len(filtered_drugs)} drugs containing '{args.generic_name}'")

    # Define selected features
    selected_features = ['product_ndc', 
                        'product_ndc_9digit',
                        'generic_name',
                        'labeler_name',
                        'brand_name',
                        'active_ingredients',
                        'marketing_start_date',
                        'listing_expiration_date',
                        'marketing_category',
                        'dosage_form',
                        'product_type',
                        'pharm_class']

    # Create a list of dictionaries with only the selected features
    filtered_data = []
    for drug in filtered_drugs:
        drug_data = {}
        for feature in selected_features:
            # Fill NA if the feature doesn't exist in the drug dictionary
            drug_data[feature] = drug.get(feature, None)
        filtered_data.append(drug_data)

    # Convert to DataFrame
    filtered_df = pd.DataFrame(filtered_data)
    
    # Create output directory if it doesn't exist
    output_dir = 'ndc_product'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save to CSV in the output directory with the generic name as filename
    output_path = os.path.join(output_dir, f"ndc_product_{args.generic_name}.csv")
    filtered_df.to_csv(output_path, index=False)
    print(f"Saved {len(filtered_df)} records to {output_path}")
    
    # Print summary and next steps
    print("\nSummary:")
    print(f"- Processed NDC directory from: {args.input_file}")
    print(f"- Found {len(filtered_drugs)} products' generic name containing '{args.generic_name}'")
    print(f"- Saved results to: {output_path}")

if __name__ == "__main__":
    main()