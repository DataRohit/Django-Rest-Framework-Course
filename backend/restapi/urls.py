# Import path to route URLs to views
from django.urls import path

# Import views.py from restapi app
from . import views

# Map the routes to respective views
urlpatterns = [
    path("", views.RestAPIHome.as_view(), name="home"),
    path("auth/", views.ObtainAuthToken.as_view()),
    path("auth/clear_expired/", views.ClearExpiredTokens.as_view()),
]
