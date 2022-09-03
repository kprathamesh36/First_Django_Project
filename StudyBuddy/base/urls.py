# To create URL's for base app so that routing can be easy

from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('/create-room/', views.create_room,name='create-room'),


]