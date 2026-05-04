import requests
import matplotlib.pyplot as plt

BASE = "http://127.0.0.1:5000"

# -----------------------------
# - SAFE API REQUEST FUNCTION -
# -----------------------------

# Sends a GET request and safely handles errors.
# Prevents crashes and prints debug info if something goes wrong.

def safe_get(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print("\nERROR calling:", url)
        print("Error:", e)
        return None


# -----------------------------
# --- PRETTY PRINT FUNCTION ---
# -----------------------------

# Formats API data nicely for console output

def print_section(title, data):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    if not data:
        print("No data returned")
        return

    if isinstance(data, dict):
        data = [data]

    for item in data:
        if isinstance(item, dict):
            for key in item:
                print(f"{key}: {item[key]}")
            print("-" * 60)
        else:
            print(item)

# -----------------------------
# -- VISUALISATION FUNCTION --
# -----------------------------

# Plots VC scores using matplotlib

def plot_vc_scores():
    data = safe_get(f"{BASE}/startups/scores")

    if not data:
        print("No VC score data available.")
        return
    
    try:
        names = [d.get("name") for d in data]
        scores = [d.get("vc_score") for d in data]

        plt.scatter(names, scores)
        plt.xticks(rotation=45, ha='right')
        plt.title("VC Scores by Startup")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Plotting error:", e)

# -----------------------------
# ------- CONSOLE MENU --------
# -----------------------------

# Let the user choose from 3 example endpoints and data visualisation
# New startups added via POST are inserted only into the Startups table.
# VC scores require related investment and therapeutic area data, so newly created startups will not appear in analytics endpoints until additional relational data is added (not shown here).


def menu():
    while True:
        print("\n=== BioVenture Console App ===")
        print("1. View all startups")
        print("2. View startup by ID")
        print("3. View VC scores")
        print("4. Plot VC scores")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print_section("ALL STARTUPS", safe_get(f"{BASE}/startups"))

        elif choice == "2":
            startup_id = input("Enter startup ID: ")
            print_section("STARTUP", safe_get(f"{BASE}/startups/{startup_id}"))

        elif choice == "3":
            print_section("VC SCORES", safe_get(f"{BASE}/startups/scores"))

        elif choice == "4":
            plot_vc_scores()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

      
# -----------------------------
# ---------- RUN APP ----------
# -----------------------------
if __name__ == "__main__":
    menu()
