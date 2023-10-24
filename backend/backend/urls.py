from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("restapi.urls")),
    path("jwtauth/", include("jwtauth.urls")),
    path("tokenauth/", include("tokenauth.urls")),
    path("products/", include("products.urls")),
]
