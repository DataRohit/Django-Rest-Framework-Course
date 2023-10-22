from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restapi/", include("restapi.urls")),
    path("restapi/products/", include("products.urls")),
]
