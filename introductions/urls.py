from django.urls import path
from . import views

app_name = "introductions"

urlpatterns = [
    path("", views.homeview, name="homeview"),
]
