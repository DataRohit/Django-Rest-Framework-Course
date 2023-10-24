# Import serializers
import random
from rest_framework import serializers
from products.models import Product
from products.validators import unique_title_validator
from tokenauth.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product__detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.ReadOnlyField(source="id")
    owner = UserPublicSerializer(source="user", read_only=True)
    title = serializers.CharField(validators=[unique_title_validator])
    sale_price = serializers.ReadOnlyField()
    discount = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name="product__detail",
        lookup_field="pk",
    )

    class Meta:
        model = Product

        fields = [
            "product_id",
            "owner",
            "title",
            "category",
            "description",
            "price",
            "sale_price",
            "discount",
            "url",
        ]
