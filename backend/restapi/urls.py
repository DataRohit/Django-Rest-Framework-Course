# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from . import views

# Map the routes to respective views
urlpatterns = [
    path("", views.RestAPIHome.as_view(), name="restapi__home"),
]
