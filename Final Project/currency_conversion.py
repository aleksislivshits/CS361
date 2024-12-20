import requests


def bailey_microservice():
    url = "http://127.0.0.1:4999/convert"
    data = {
        "budgets": {
            "USD": {
                "actual_income": 100,
                "expected_income": 150,
                "actual_expenses": [{"name": "Rent", "amount": 50}, {"name": "Utilities", "amount": 20}],
                "expected_expenses": [{"name": "Groceries", "amount": 30}]
            }
        },
        "currency": "AUD"
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"error: {response.status_code}")


if __name__ == "__main__":
    bailey_microservice()