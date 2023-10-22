# Imports
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from rest_framework import parsers, renderers
from restapi.models import ExpiringToken
from restapi.serializers import ExpiringTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ExpiringTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = ExpiringToken.objects.get_or_create(user=user)
        return Response({"token": token.key})


# Function for home page view
@api_view(["POST"])
def restapi_home(request, *args, **kwargs):
    # Get the body of the request
    body = request.data

    if not body:
        return Response(
            {"error": "No JSON Body Received!"}, status=status.HTTP_BAD_REQUEST
        )

    # Create a dictionary to store the response data
    response_data = {}

    # Convert the byte string to a dictionary
    try:
        body_dict = dict(body)

        response_data["content_type"] = request.content_type
        response_data["query_params"] = dict(request.GET)
        response_data["request_body"] = body_dict

    except ValueError:
        response_data = {"error": "Invalid JSON Payload Received!", "body": body}

    # Return JSON data
    return Response(response_data)
