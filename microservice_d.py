# Changed to DEBT TRACKING Microservice:

from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load budget data
def load_budget_data(filename='budget.json'):
    with open(filename, 'r') as f:
        return json.load(f)


@app.route('/debt-tracker', methods=['GET'])
def debt_tracker():
    budget_data = load_budget_data()
    debt = sum([category['amount'] for category in budget_data if category['amount'] < 0])  # Assuming negative amounts are debt
    return jsonify({"total_debt": debt})


if __name__ == '__main__':
    app.run(port=5004)
