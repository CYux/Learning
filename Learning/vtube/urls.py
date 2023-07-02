from django.urls import path
from . import views

app_name = "vtube"

urlpatterns = [
    path("", views.index, name="index"),
    path("play-video", views.play, name="play")
]