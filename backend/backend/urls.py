from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restapi/auth/", obtain_auth_token),
    path("restapi/", include("restapi.urls")),
    path("restapi/products/", include("products.urls")),
]
