# Import json to convert byte string to JSON
import json

# Import JsonResponse to return JSON data
from django.http import JsonResponse


# Function for home page view
def home(request, *args, **kwargs):
    # Get the query parameters
    # Returns a dictionary
    query_params = request.GET

    # Get the body of the request
    # Returns a byte string of json data
    body = request.body

    # If body is empty, set it to an empty string
    if not body:
        return JsonResponse({"error": "No JSON Body Received!"}, status=400)

    # Convert the byte string to a dictionary
    try:
        # If the body is valid JSON, load the data
        body_dict = json.loads(body)

        # Add the content type to the dictionary
        body_dict["content_type"] = request.content_type

        # Add the headers to the dictionary
        body_dict["headers"] = dict(request.headers)

        # Add the query parameters to the dictionary
        body_dict["query_params"] = dict(query_params)

    except ValueError:
        body_dict = {"error": "Invalid JSON Payload Received!", "body": body}

    # Return JSON data
    return JsonResponse(body_dict)
