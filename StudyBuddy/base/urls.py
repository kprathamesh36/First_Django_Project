# To create URL's for base app so that routing can be easy

from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('rooms/<str:pk>/',views.rooms,name='rooms'),


]