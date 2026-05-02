import requests
import matplotlib.pyplot as plt

response = requests.get("http://127.0.0.1:5000/portfolio/rankings")
data = response.json()

names = [d["name"] for d in data]
scores = [d["vc_score"] for d in data]

plt.scatter(names, scores)
plt.xticks(rotation=45, ha='right')
plt.title("VC Scores by Startup")
plt.tight_layout()
plt.show()