# main.py - orchestrates the Biosafety Check workflow

# Import functions to fetch FDA data and save results
from api_utils import get_fda_data
from file_utils import save_results_to_file


# Ask the user for a drug name to query
drug_name = input("Enter a drug name to check safety reports: ")

# Fetch up to 500 FDA adverse events reports for the specified drug
results = get_fda_data(drug_name)

# Generate and save a readable safety summary to 'results.txt'
save_results_to_file(results, drug_name)


# Notify the user that the programme has finished
print("Safety report check complete.")

