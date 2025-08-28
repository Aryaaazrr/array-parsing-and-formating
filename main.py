from flask import Flask, request, jsonify

app = Flask(__name__)

def reformat_data(data):
    result = {}
    for item in data:
        category = item.get("category")
        sub_category = item.get("sub_category")

        if category not in result:
            result[category] = {}
        if sub_category not in result[category]:
            result[category][sub_category] = []

        result[category][sub_category].append({
            "id": item.get("id"), "name": item.get("name")
        })
    return result

@app.route("/reformat", methods=["POST"])
def reformat_endpoint():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({"error": "Input must be a list of dictionaries"}), 400
    
    try:
        reformatted = reformat_data(data)
        return jsonify(reformatted)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
