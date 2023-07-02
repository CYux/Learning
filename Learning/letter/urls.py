from django.urls import path
from . import views

app_name = "letter"

urlpatterns = [
    path("", views.index, name="index")
]