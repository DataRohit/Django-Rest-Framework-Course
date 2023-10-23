from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tokenauth/", include("tokenauth.urls")),
    path("restapi/", include("restapi.urls")),
    path("products/", include("products.urls")),
]
