from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_post),
    path("ajax/getPosts/", views.getPosts, name='getPosts'),
]
