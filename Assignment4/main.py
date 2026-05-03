import requests
import matplotlib.pyplot as plt


BASE = "http://127.0.0.1:5000"

def print_section(title, data):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    for item in data:
        # pretty key-value format instead of raw dict
        for key, value in item.items():
            print(f"{key:25}: {value}")
        print("-" * 60)


print_section("ALL STARTUPS", requests.get(f"{BASE}/portfolio").json())

print_section("STARTUP ID 1", requests.get(f"{BASE}/portfolio/startup/1").json())

print_section("VC SCORED STARTUPS", requests.get(f"{BASE}/portfolio/rankings").json())


response = requests.get("http://127.0.0.1:5000/portfolio/rankings")
data = response.json()

names = [d["name"] for d in data]
scores = [d["vc_score"] for d in data]

plt.scatter(names, scores)
plt.xticks(rotation=45, ha='right')
plt.title("VC Scores by Startup")
plt.tight_layout()
plt.show()