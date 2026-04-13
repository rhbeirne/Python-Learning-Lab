#4-13

import requests
import json

print("--- Contacting the API Waiter ---")

# This is a free, public API that generates fake user data for testing
api_url = "https://jsonplaceholder.typicode.com/users/1"

# TODO 1: Use the requests library's .get() tool to ask the API for data.
# Pass the 'api_url' into it, and save it to a variable called 'response'.
response = requests.get(api_url)


# TODO 2: The waiter's data is stored inside a special property called '.text'.
# Print out 'response.text' to see the raw JSON string they brought back!
print(response.text)

response_dict = json.loads(response.text)

print (response_dict["website"])