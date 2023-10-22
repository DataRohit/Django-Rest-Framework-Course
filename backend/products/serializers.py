# Import serializers
from rest_framework import serializers
from rest_framework import reverse
from products.models import Product


# Define a serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    # Include properties explicitly
    sale_price = serializers.ReadOnlyField()
    discount = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name="search_modify_product", lookup_field="pk"
    )

    class Meta:
        # Specify the model to be serialized
        model = Product

        # Serialize all fields in the model
        fields = "__all__"
