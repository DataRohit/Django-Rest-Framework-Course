# Imports
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status, generics


from restapi.models import ExpiringToken
from rest_framework.authtoken.views import ObtainAuthToken
from restapi.serializers import *

from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from restapi.permissions import IsTokenEditorPermission
from rest_framework.response import Response


class RestAPIHome(APIView):
    def post(self, request, *args, **kwargs):
        user_post_data = request.data

        response_data = {
            "content_type": request.content_type,
            "query_params": dict(request.GET),
            "request_body": user_post_data,  # Return the user's POST JSON data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class ObtainAuthToken(ObtainAuthToken):
    serializer_class = ExpiringTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = ExpiringToken.objects.get_or_create(user=user)
        return Response({"token": token.key})


class ClearExpiredTokens(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, IsTokenEditorPermission]
    serializer_class = ExpiringTokenSerializer

    def get_queryset(self):
        return ExpiringToken.objects.filter(expiration__lt=timezone.now())

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
