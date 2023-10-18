# Imports
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Function for home page view
@api_view(["POST"])
def home(request, *args, **kwargs):
    # Get the body of the request
    body = request.data

    if not body:
        return Response(
            {"error": "No JSON Body Received!"}, status=status.HTTP_BAD_REQUEST
        )

    # Create a dictionary to store the response data
    response_data = {}

    # Convert the byte string to a dictionary
    try:
        body_dict = dict(body)

        response_data["content_type"] = request.content_type
        response_data["query_params"] = dict(request.GET)
        response_data["request_body"] = body_dict

    except ValueError:
        response_data = {"error": "Invalid JSON Payload Received!", "body": body}

    # Return JSON data
    return Response(response_data)
