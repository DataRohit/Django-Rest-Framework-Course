# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from . import views

# Map the routest to respective views
urlpatterns = [
    path("", views.ProductHomeView.as_view(), name="home"),
    path(
        "product/<uuid:pk>/", views.ProductSearchView.as_view(), name="search_product"
    ),
    path(
        "product/<uuid:pk>/update",
        views.ProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "product/<uuid:pk>/delete",
        views.ProductDeleteView.as_view(),
        name="delete_product",
    ),
    path("list/", views.ProductListView.as_view(), name="list_product"),
    path("create/", views.ProductCreateView.as_view(), name="create_product"),
]
