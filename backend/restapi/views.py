# Import JsonResponse to return JSON data
from django.http import JsonResponse


# Function for home page view
def home(request, *args, **kwargs):
    # Return JSON data
    return JsonResponse(
        {"info": "Django REST API", "name": "Django REST API"}, status=200
    )
