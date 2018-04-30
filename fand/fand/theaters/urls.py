"""fand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'theaters'

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.list_movies, name='movies-list'),
    path('movies/<int:pk>', views.movie, name='movies-detail'),
    path('theaters/', views.list_theaters, name='theaters-list'),
    path('theaters/<slug:pk>', views.theater, name='theaters-detail'),
    path('showtimes/', views.list_showtimes, name='showtimes-list'),
    path('api/<slug:slug>/', views.api, name='api'),
]
