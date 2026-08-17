# file_utils.py - takes data and saves it to a file (results.txt)

# Import counter to count occurences of reactions 
from collections import Counter

# Function to generate and save a safety report from API results
def save_results_to_file(results, drug_name):

    """
    Takes a list of dictionaries from the API and saves a readable safety report.
    - Counts reactions
    - Flags serious reactions
    """
    # If no results were found notify the user and exit the function
    if not results:
        print(f"No safety reports found for {drug_name}")
        return

    # Count reactions in lists
    all_reactions = []
    serious_reactions = []

    # Loop through each case in results
    for r in results:
        reactions_list = [rx.strip() for rx in r["reactions"].split(",") if rx]
        all_reactions.extend(reactions_list)


        # Loop through reactions, check for serious reactions and append to new variable
        for rx in reactions_list:
            if rx.lower() in ["death", "hospitalization", "life-threatening"]:
                serious_reactions.append(rx)

    # Count occurrences of each reaction
    reaction_counts = Counter(all_reactions)

    # Use .most_common() method to get top 5 most frequent reactions
    top_reactions = reaction_counts.most_common(5)


    # Write safety summary to file
    with open("results.txt", "w") as f:

        # Write report header with drug name
        f.write(f"{drug_name} Safety Summary:\n")
        f.write("-" * 50 + "\n")

        # Write total number of reports analysed
        f.write(f"Total reports analysed: {len(results)}\n\n")

        # Write the most common report reactions
        f.write(f"Top reported reactions: \n")
        for rx, count in top_reactions:
             f.write(f" - {rx} ({count})\n")

        # Write summary of most serious report reactions
        f.write("\n")
        f.write(f"Serious reactions found: {len(serious_reactions)}\n")
       
        if serious_reactions:

            # List unique serious reactions using "set" to remove duplicates
            f.write(f"Details: {', '.join(set(serious_reactions))}\n")
        else:
             
             # If no serious reaction indicate to user
             f.write("Details: None\n")

        # Write footer separator 
        f.write("-" * 50 + "\n\n")

    # Notify the user that the file has been saved 
    print("Results saved to results.txt")