from django.urls import path
from . import views

app_name = "pcases"

urlpatterns = [
    path("", views.pcaseview, name="pcase"),
]
