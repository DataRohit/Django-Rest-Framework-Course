# Imports
from rest_framework.response import Response
from rest_framework import status


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class RestAPIHome(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_post_data = request.data

        response_data = {
            "content_type": request.content_type,
            "query_params": dict(request.GET),
            "request_body": user_post_data,  # Return the user's POST JSON data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
