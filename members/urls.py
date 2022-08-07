from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path("", views.member_intro, name="member"),
]
