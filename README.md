Communication Contract:

How does one REQUEST data from the implemented microservice?
- There will be an HTTP GET request at the endpoint of the microservice. 
- Example call:
   response = requests.get('(http://127.0.0.1:5000/convert)')

- So the JSON data will update the budget file and send a POST request to update the budget file's data with the inputted values:

data = {
  "budgets": {}
    "USD": 100,
    "EUR": 200
  },
  "currency": "AUD"
}

How does one RECEIVE data from the implemented microservice?
- Once an HTTP GET request is seen by the program, the microservice will send the requested data back. The requests.get('http://localhost:5000/convert') will send a GET request to that URL and then then, once the response is successful, it will process the JSON data.

response = requests.post(url, json=data)
if response.status_code == 200:
  print(response.json())
else:
  print(f"error: {response.status_code})


UML Diagram:


<img width="687" alt="Screenshot 2024-11-18 at 5 04 40 PM" src="https://github.com/user-attachments/assets/2aa7c49d-492a-4fe0-8045-adc32edb5725">
