# Import serializers
from rest_framework import serializers
from products.models import Product


# Define a serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = Product

        # Serialize all fields in the model
        fields = [
            "id",
            "title",
            "category",
            "description",
            "price",
            "sale_price",
            "discount",
        ]
