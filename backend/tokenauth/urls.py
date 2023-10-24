# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from tokenauth import views

# Map the routes to respective views
urlpatterns = [
    path("token/", views.ObtainAuthToken.as_view(), name="tokenauth__token"),
]
