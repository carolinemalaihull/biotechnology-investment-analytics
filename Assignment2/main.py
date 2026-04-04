 # main.py

from api_utils import get_fda_data
from file_utils import save_results_to_file


# 1. Ask the user for a drug name
drug_name = input("Enter a drug name to check safety reports: ")


# 2. Get data from the FDA API
results = get_fda_data(drug_name)


# 3. Save the results to a file
save_results_to_file(results, drug_name)


# 4. Tell the user the program is finished
print("Safety report check complete.")

