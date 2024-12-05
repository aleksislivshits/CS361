import requests


def microservice_a_test():
    url = "http://127.0.0.1:5001/sort-budget"
    data = {
        "categories": [
                 {"name": "Food", "amount": 200},
                 {"name": "Utilities", "amount": 150},
                 {"name": "Entertainment", "amount": 300}
             ]
        }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"error: {response.status_code}")


if __name__ == "__main__":
    microservice_a_test()



# import unittest
# import json
# from flask import Flask
# from microservice_a import
#
# # Assuming the original Flask app code is in a file named app.py
# from app import app
#
# class BudgetSortTestCase(TestCase):
#     def create_app(self):
#         # Create a new instance of the Flask app for testing
#         return app
#
#     def test_sort_budget(self):
#         # Sample data to test the sorting functionality
#         test_data = {
#             "categories": [
#                 {"name": "Food", "amount": 200},
#                 {"name": "Utilities", "amount": 150},
#                 {"name": "Entertainment", "amount": 300}
#             ]
#         }
#
#         # Send a POST request to the /sort-budget endpoint
#         response = self.client.post('/sort-budget', data=json.dumps(test_data), content_type='application/json')
#
#         # Assert the response status code
#         self.assertEqual(response.status_code, 200)
#
#         # Assert the sorted categories in the response
#         expected_sorted_categories = [
#             {"name": "Entertainment", "amount": 300},
#             {"name": "Food", "amount": 200},
#             {"name": "Utilities", "amount": 150}
#         ]
#         self.assertEqual(response.json['sorted_categories'], expected_sorted_categories)
#
#     def test_missing_categories(self):
#         # Test for missing 'categories' in the request data
#         response = self.client.post('/sort-budget', data=json.dumps({}), content_type='application/json')
#
#         # Assert the response status code and error message
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(response.json['error'], "Missing 'categories' in request data")
#
# if __name__ == '__main__':
#     unittest.main()
