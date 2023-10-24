from django.contrib import admin
from django.urls import include, path
from rest_framework.response import Response
from rest_framework import status


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        lambda request: Response(
            {
                "message": "Hello from the DataRohit!",
            },
            status=status.HTTP_200_OK,
        ),
    ),
    path("jwtauth/", include("jwtauth.urls")),
    path("tokenauth/", include("tokenauth.urls")),
    path("restapi/", include("restapi.urls")),
    path("products/", include("products.urls")),
]
