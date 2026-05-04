from flask import Flask, jsonify, request
from config import get_db_connection
from db_utils import get_startups, get_top_startups, get_sector_allocation, get_startup_by_id, get_score, post_new_startup, delete_startup


app = Flask(__name__)

app.json.sort_keys = False

#-------------------------
#-- BASIC GET ENDPOINTS --
#-------------------------


@app.route("/")
def home():
    return jsonify({"message": "BioVenture API is running"})

@app.route("/startups")
def startups():
    data = get_startups()
    return jsonify(data)

@app.route("/startups/top-startups")
def top_investment_startups():
    data = get_top_startups()
    return jsonify(data)

@app.route("/sectors/allocation")
def sector_allocation():
    data = get_sector_allocation()
    return jsonify(data)

@app.route("/startups/<int:startup_id>")
def startup_by_id(startup_id):
    data = get_startup_by_id(startup_id)
    if not data:
        return jsonify({"message": "Startup not found"}), 404
    return jsonify(data)

#-------------------------
#----- GET VC SCORES -----
#-------------------------

# Add function to score startups on the basis of their overall profile
def calculate_vc_score(row):
    return (
        (float(row["total_funding"]) / 10)
        + (row["rounds"] * 5)
        + row["stage_score"]
        + (row["areas"] * 3)
    )

@app.route("/startups/scores")
def scores():
    try:
        data = get_score()

        if not data:
            return jsonify({"message": "No startup data found in database"}), 404

        for row in data:
            row["vc_score"] = calculate_vc_score(row)

        return jsonify(data), 200
    
    except Exception as e:
        print(f"Error generating score: {e}")
        return jsonify({
            "message": "Failed to generate VC score",
            "error": str(e)
        }), 500

#-------------------------
#----- POST REQUEST ------
#-------------------------

@app.route("/startups", methods=["POST"])
def add_startup():
    data = request.get_json()

    required_fields = ["name", "technology", "latest_investment_stage"]
    if not all(data.get(field) for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    
    result = post_new_startup(data)

    if "error" in result:
        return jsonify(result), 500
    
    return jsonify(result), 200

#-------------------------
#---- DELETE STARTUP -----
#-------------------------

@app.route("/startups/<int:startup_id>", methods=["DELETE"])
def remove_startup(startup_id):
    result = delete_startup(startup_id)
    
    if result.get("message") == "Startup not found":
        return jsonify(result), 404
    
    if "error" in result:
        return jsonify(result), 500
    
    return jsonify(result), 200



if __name__ == '__main__':
   app.run(debug=True)
