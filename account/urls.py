
from django.contrib import admin
from django.urls import path

from account import views

urlpatterns = [
    path('signup/', views.user_register, name='signup'),
    path('home/', views.user_register, name='home'),
]
