# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from products import views

# Map the routes to respective views
urlpatterns = [
    path("", views.ProductHomeView.as_view(), name="product__home"),
    path(
        "<uuid:pk>/",
        views.ProductDetailView.as_view(),
        name="product__detail",
    ),
    path(
        "<uuid:pk>/update/",
        views.ProductUpdateView.as_view(),
        name="product__update",
    ),
    path(
        "<uuid:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product__delete",
    ),
    path("list/", views.ProductListView.as_view(), name="product__list"),
    path("create/", views.ProductCreateView.as_view(), name="product__create"),
    path("search/", views.ProductSearchView.as_view(), name="product__search"),
]
