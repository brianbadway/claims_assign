from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index), # to main page
    path('to_assign', views.to_assign), # to assign page
    path('adj_assign', views.adj_assign), # to assign page
]