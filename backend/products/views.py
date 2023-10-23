from random import randint
from rest_framework.response import Response
from rest_framework import status, generics
from products.models import Product
from products.serializers import ProductSerializer
from tokenauth.mixins import ProductEditorPermissionMixin
from django.db.models import Q


class ProductHomeView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        product_count = Product.objects.count()
        if product_count > 0:
            random_index = randint(0, product_count - 1)
            return Product.objects.all()[random_index]
        return None


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(ProductEditorPermissionMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []


class ProductUpdateView(ProductEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(ProductEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response(
            {"message": "Product Deleted Successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        if query:
            filter = (
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(category__icontains=query)
            )
            return Product.objects.filter(filter)
        return Product.objects.none()
