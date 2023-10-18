# Import
from random import randint
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from products.serializers import *


# Function for getting a random product
@api_view(["GET"])
def home(request, *args, **kwargs):
    # Count the number of products in the Product model
    product_count = Product.objects.count()

    # If there are products in the Product model
    if product_count > 0:
        # Get a random product index
        random_index = randint(0, product_count - 1)

        # Query all products and get the product at the random index
        query_product = Product.objects.all()[random_index]

        # Serialize the product using the serializer
        serializer = ProductSerializer(query_product)

        # Return the serialized data
        return Response(serializer.data)

    return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)


# Function to search for a product using a query parameter
@api_view(["GET"])
def search_product(request, *args, **kwargs):
    # Get the query parameter
    query_parameter = request.GET.get("title")

    if not query_parameter:
        return Response(
            {"error": "Query parameter not found!"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not query_parameter.strip():
        return Response(
            {"error": "Invalid query parameter!"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Get the products from the Product model
    query_products = Product.objects.filter(title__icontains=query_parameter)[:5]

    if query_products:
        # Serialize the products using the serializer
        serializer = ProductSerializer(query_products, many=True)
        return Response({"products": serializer.data})

    return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
