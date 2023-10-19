from random import randint
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer


class HomeView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        product_count = Product.objects.count()
        if product_count > 0:
            random_index = randint(0, product_count - 1)
            return Product.objects.all()[random_index]
        return None


class SearchProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddProductView(generics.CreateAPIView):
    serializer_class = ProductSerializer
