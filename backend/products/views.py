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

    return Response(
        {"error": "Products Not Available."}, status=status.HTTP_404_NOT_FOUND
    )


# Function to search for a product using a query parameter
@api_view(["GET"])
def search_product(request, *args, **kwargs):
    # Get the query parameters
    query_params = {
        "title__icontains": request.GET.get("title"),
        "category__icontains": request.GET.get("category"),
        "description__icontains": request.GET.get("description"),
    }

    # Remove empty parameters
    filters = {key: value for key, value in query_params.items() if value}

    if not filters:
        return Response(
            {"error": "No query parameters provided!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Get the products from the Product model with applied filters
    query_products = Product.objects.filter(**filters)[:5]

    if query_products:
        # Serialize the products using the serializer
        serializer = ProductSerializer(query_products, many=True)
        return Response({"products": serializer.data})

    return Response({"error": "No products found."}, status=status.HTTP_404_NOT_FOUND)


# Function to add a product
@api_view(["POST"])
def add_product(request, *args, **kwargs):
    # Serialize the request data
    serializer = ProductSerializer(data=request.data)

    # If the data is valid
    if serializer.is_valid():
        # Save the data
        product = serializer.save()

        # Serialize the added product data
        serialized_product = ProductSerializer(product)
        return Response(
            {
                "success": "Product added successfully",
                "product": serialized_product.data,
            },
            status=status.HTTP_201_CREATED,
        )

    else:
        # If the data is not valid, return an error response with validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
