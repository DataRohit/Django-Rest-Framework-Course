from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from restapi.views import ObtainAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restapi/auth/", ObtainAuthToken.as_view()),
    path("restapi/", include("restapi.urls")),
    path("restapi/products/", include("products.urls")),
]
