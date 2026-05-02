from flask import Flask, jsonify
from config import get_db_connection
from db_utils import get_db_connection, get_portfolio, get_top_startups, get_sector_allocation, get_startup_by_id, get_score


app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "BioVenture API is running"})

@app.route("/portfolio")
def portfolio():
    data = get_portfolio()
    return jsonify(data)

@app.route("/portfolio/top-startups")
def top_statups():
    data = get_top_startups()
    return jsonify(data)

@app.route("/portfolio/sector-allocation")
def top_sectors():
    data = get_sector_allocation()
    return jsonify(data)

@app.route("/portfolio/startup/<int:startup_id>")
def startup_by_id(startup_id):
    data = get_startup_by_id(startup_id)
    return jsonify(data)

@app.route("/portfolio/rankings")
def rankings():
    data = get_score()

    for row in data:
        row["vc_score"] = (
            (float(row["total_funding"]) / 10)
            + (row["rounds"] * 5)
            + row["stage_score"]
            + (row["areas"] * 3)
        )
    return jsonify(data)


if __name__ == '__main__':
   app.run(debug=True)
