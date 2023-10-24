from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status, generics
from tokenauth.models import ExpiringToken
from rest_framework.authtoken.views import ObtainAuthToken
from tokenauth.serializers import ExpiringTokenSerializer


import logging

logger = logging.getLogger(__name__)


# Create your views here.
class ObtainAuthToken(ObtainAuthToken):
    serializer_class = ExpiringTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = ExpiringToken.objects.get_or_create(user=user)
        return Response({"token": token.key})
