from django.urls import path
from . import views

app_name = "workscopes"

urlpatterns = [
    path("", views.workscope_list, name="workscope_list"),
]
