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


class SearchProductView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        filters = {}
        query_params = {
            "title__icontains": self.request.GET.get("title"),
            "category__icontains": self.request.GET.get("category"),
            "description__icontains": self.request.GET.get("description"),
        }
        filters = {key: value for key, value in query_params.items() if value}

        return Product.objects.filter(**filters) if filters else Product.objects.none()


class AddProductView(generics.CreateAPIView):
    serializer_class = ProductSerializer
