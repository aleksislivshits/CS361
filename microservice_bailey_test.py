from flask import Flask, request, jsonify

app = Flask(__name__)

supported_currencies = ["USD", "EUR", "AUD", "CAD"]


@app.route('/convert', methods=['POST'])  # This will handle the POST requests
def convert_currency():
    data = request.json
    budgets = data.get('budgets', {})
    goal_currency = data.get('currency', '')

    if goal_currency not in supported_currencies:  # Test that the currency that they want to convert to is there
        return jsonify({"error": "Currency is not supported yet..."}), 400

# Current conversion rates as of November 16th, 2024 cited from: https://www.x-rates.com/table/?from=USD&amount=1
    conversion_rates = {
        "USD": 1.0,
        "AUD": 1.53,
        "EUR": 0.94,
        "CAD": 1.4
    }
    converted_budgets = {}
    for currency, amount in budgets.items():
        if currency in conversion_rates:
            converted_amount = amount * (conversion_rates[goal_currency] / conversion_rates[currency])
            converted_budgets[currency] = round(converted_amount, 2)  # Need to round for consistency
    if not converted_budgets:
        return jsonify({"error": "No valid conversions made!"}), 400

    return jsonify({"converted_budgets": converted_budgets})  # Return of a JSON response that has the converted budget
    # values.


if __name__ == '__main__':
    app.run(debug=True)
