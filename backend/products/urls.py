# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from . import views

# Map the routest to respective views
urlpatterns = [
    path("", views.ProductHomeView.as_view(), name="home"),
    path(
        "search_product/<uuid:pk>/",
        views.SearchProductView.as_view(),
        name="search_product",
    ),
    path("add_product/", views.AddProductView.as_view(), name="add_product"),
]
