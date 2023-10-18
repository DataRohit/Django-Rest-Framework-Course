# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from . import views

# Map the routest to respective views
urlpatterns = [
    path("", views.home, name="home"),
]
