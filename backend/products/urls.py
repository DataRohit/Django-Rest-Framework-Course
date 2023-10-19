# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from . import views

# Map the routest to respective views
urlpatterns = [
    path("", views.home, name="home"),
    path("search_product/", views.search_product, name="search_product"),
    path("add_product/", views.add_product, name="add_product"),
]
