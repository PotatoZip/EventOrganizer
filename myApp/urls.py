from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
]