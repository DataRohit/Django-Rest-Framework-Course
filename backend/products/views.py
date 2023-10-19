from random import randint
from rest_framework.response import Response
from rest_framework import status, generics, authentication, permissions
from products.models import Product
from products.serializers import ProductSerializer


class ProductHomeView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        product_count = Product.objects.count()
        if product_count > 0:
            random_index = randint(0, product_count - 1)
            return Product.objects.all()[random_index]
        return None


class ProductSearchView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get the instance you want to update
        instance = self.get_object()

        # Create the serializer with the instance as initial data
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # Get the instance you want to update
        instance = self.get_object()

        # Create the serializer with the instance and request data
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
