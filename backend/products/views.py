# Import serializer
from django.core.serializers import serialize

# Import json to convert model to JSON
import json

# Import JsonResponse to return JSON data
from django.http import JsonResponse

# Import for converting model to JSON
from django.forms.models import model_to_dict

# Import the Product model
from products.models import Product


# Function for home page view
def home(request, *args, **kwargs):
    # Get a random record from the Product model
    query_product = Product.objects.order_by("?").first()

    # Check if data exists
    if query_product:
        # Convert model to JSON
        query_product = model_to_dict(query_product)

        # Return JSON data
        return JsonResponse({"product": query_product})

    # Return an error message for product not found
    return JsonResponse({"error": "Product not found."}, status=404)


# Function to search for a product using the query parameter
def search_product(request, *args, **kwargs):
    # Get the query parameter
    query_parameter = request.GET

    # If query parameter not exists
    if not query_parameter:
        # Return an error message
        return JsonResponse({"error": "Query parameter not found!"}, status=404)

    # If invalid query parameter
    if not query_parameter.get("title"):
        # Return an error message
        return JsonResponse({"error": "Invalid query parameter!"}, status=404)

    # If query parameter exists
    # Get the query parameter
    query_parameter = query_parameter.get("title")

    # Get the product from the Product model
    query_product = json.loads(
        serialize(
            "json", Product.objects.filter(title__icontains=query_parameter).all()[:5]
        )
    )

    # Return back the query parameter
    return JsonResponse({"products": query_product})
