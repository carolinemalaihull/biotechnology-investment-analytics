# imports the requests module from the standard python library which simplifies interacting with APIs 
import requests

# api_utils.py - calls the FDA API and returns data
# Define a function that retrieves adverse reactionst to a user defined drug

def get_fda_data(event):
    """
    Fetch up to 500 FDA adverse event reports for a given event name.
    Returns a list of dictionaries with case_id, reactions, and drugs.
    """
    url = f"https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:{event}&limit=500"
    response = requests.get(url) 
    # use get method and requests library to fetch data from the url
    data = response.json()  
    # parse JSON

    results = []
    for case in data.get("results", []):  # loop through cases
        # get values or defaults
        case_id = case.get("safetyreportid", "Unknown ID")
        
        #defines variable called "has_reactions" to define whether reactions are present for particular FDA reports
        has_reactions =len(case.get("patient", {}).get("reaction", []))>0

        if has_reactions:
            reactions = ", ".join([r.get("reactionmeddrapt", "") for r in case.get("patient", {}).get("reaction", [])])
        else:
            reactions = "No reactions reported"

        drugs = ", ".join([d.get("medicinalproduct", "") for d in case.get("patient", {}).get("drug", [])])
        
        results.append({"case_id": case_id, "reactions": reactions, "drugs": drugs})

    return results

