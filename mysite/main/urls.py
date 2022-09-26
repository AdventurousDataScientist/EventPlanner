from django.urls import path
from . import views

urlpatterns = [
    path("index/<int:id>", views.index, name="index"),
    path("create", views.create_event, name="create_event"),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),

]