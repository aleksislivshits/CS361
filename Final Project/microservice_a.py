# Implemented by Bailey Thibodeaux, sorts my categories
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

def load_sorted_budget(filename = 'sorted.json'):
    with open(filename, 'r') as file:
        return json.load(file)

@app.route('/sort-budget', methods=['POST'])
def sort_budget():
    data = request.get_json()

    if not data or 'categories' not in data:
        return jsonify({"error": "Missing 'categories' in request data"}), 400

    categories = data['categories']
    sorted_categories = sorted(categories, key=lambda x: x['amount'], reverse=True)
    return jsonify({"sorted_categories": sorted_categories})


if __name__ == '__main__':
    app.run(port=5001)
