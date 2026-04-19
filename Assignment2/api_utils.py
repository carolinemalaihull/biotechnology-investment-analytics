# This programme uses open FDA API which provides public data about drug safety reports
# No key is required for basic usage of this API
# The API returns data in JSON format which is converted into Python dictionaries

# Import the request library to simplify making API calls 
# Requests module sends HTTP requests to the API
# Installed by running pip install requests
import requests

# api_utils.py - calls the FDA API and returns data

# Define a function that retrieves adverse reactions to a user defined drug
def get_fda_data(event):
    """
    Fetch up to 500 FDA adverse event reports for a given event name.
    Returns a list of dictionaries with case_id, reactions, and drugs.
    """
    url = f"https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:{event}&limit=500"
    
    # Send a get request to the API
    response = requests.get(url) 

    # Parse JSON
    data = response.json()  
    
    results = []
    # Loop through cases
    for case in data.get("results", []):  
        # Get values or defaults
        case_id = case.get("safetyreportid", "Unknown ID")
        
        # Check if the case has any reactions (True or False)
        has_reactions = len(case.get("patient", {}).get("reaction", []))>0

        # If reactions exist, extract their names and join them into a comma-separated string
        if has_reactions:
            reactions = ", ".join([r.get("reactionmeddrapt", "") for r in case.get("patient", {}).get("reaction", [])])

        # If no reactions exist return a default message
        else:
            reactions = "No reactions reported"

        # Safely get the drug list, extract drug names and join them into a comma-separated string
        drugs = ", ".join([d.get("medicinalproduct", "") for d in case.get("patient", {}).get("drug", [])])
        
        # Add this case's processed data (case_id, reactions, drugs) to the results list

        results.append({"case_id": case_id, "reactions": reactions, "drugs": drugs})

    # Return the complete list of processed cases
    return results

