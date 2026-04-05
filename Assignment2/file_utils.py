# file_utils.py - takes data and saves it to a file (results.txt)

from collections import Counter

def save_results_to_file(results, drug_name):
    
    """
    Takes a list of dictionaries from the API and saves a readable safety report.
    - Counts reactions
    - Flags serious reactions
    - Lists unique co-administered drugs
    """

    if not results:
        print(f"No safey reports found for {drug_name}")
        return

    # Count reactions in lists
    all_reactions = []
    serious_reactions = []


    for r in results:
        reactions_list = [rx.strip() for rx in r["reactions"].split(",") if rx]
        all_reactions.extend(reactions_list)


    #Check for serious reactions
        for rx in reactions_list:
            if rx.lower() in ["death", "hospitalization", "life-threatening"]:
                serious_reactions.append(rx)

    # count occurences of each reaction
    reaction_counts = Counter(all_reactions)
    top_reactions = reaction_counts.most_common(5)


    #Write results to file
    with open("results.txt", "w") as f:
        f.write(f"{drug_name} Safety Summary:\n")
        f.write("-" * 50 + "\n")
        f.write(f"Total reports analyzed: {len(results)}\n\n")
        f.write(f"Top reported reactions: \n")
        for rx, count in top_reactions:
             f.write(f" - {rx} ({count})\n")

        f.write("\n")
        f.write(f"Serious reactions found: {len(serious_reactions)}\n")
        if serious_reactions:
            f.write(f"Details: {', '.join(set(serious_reactions))}\n")
        else:
             f.write("Details: None\n")

        f.write("-" * 50 + "\n\n")


    print("Results saved to results.txt")