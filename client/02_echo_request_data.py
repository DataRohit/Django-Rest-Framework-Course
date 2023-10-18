# Import the pretty print function
from pprint import pprint

# Import requests for making HTTP requests
import requests

# Initialize the endpoint URL
endpoint = "http://localhost:8000/restapi/"

# Make a GET request to the endpoint and store the response
get_response = requests.get(
    endpoint, params={"name": "Django REST API"}, json={"query": "Django REST API"}
)

# Print the status code of the response
print(get_response.status_code)

# Print the response payload
pprint(get_response.json())
