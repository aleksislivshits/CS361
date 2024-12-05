# # Yearly savings projection or progress bar!
#

from flask import Flask, jsonify
import json

app = Flask(__name__)


# Load budget data
def load_budget_data(filename='budget.json'):
    with open(filename, 'r') as f:
        return json.load(f)


@app.route('/progress-bar', methods=['GET'])
def progress_bar():
    budget_data = load_budget_data()
    total_budget = sum([category['amount'] for category in budget_data])
    total_spent = sum([category['amount'] for category in budget_data if category['amount'] > 0])

    progress = (total_spent / total_budget) * 100 if total_budget > 0 else 0
    return jsonify({"progress": progress})


if __name__ == '__main__':
    app.run(port=5002)
