from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('belajar1/', views.belajar1, name='belajar1'),
    path('home/', views.home, name='home'),
]