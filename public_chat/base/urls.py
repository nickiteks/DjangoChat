from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('add/',views.add_post),
#TODO 43 49
]