# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from . import views

# Map the routes to respective views
urlpatterns = [
    path("", views.ProductHomeView.as_view(), name="home"),
    path(
        "<uuid:pk>/",
        views.ProductSearchUpdateDestroyView.as_view(),
        name="search_modify_product",
    ),
    path("list/", views.ProductListView.as_view(), name="list_product"),
    path("create/", views.ProductCreateView.as_view(), name="create_product"),
    path("search/", views.ProductSearchView.as_view(), name="search_product"),
]
