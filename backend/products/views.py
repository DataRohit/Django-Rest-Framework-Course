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
