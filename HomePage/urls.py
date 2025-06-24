from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.Homepage, name='homepage'),
    path('user-detials/<int:pk>/', views.user_detail, name='user_detail'),
    
]