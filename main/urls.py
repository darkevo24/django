from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('', views.index,name="index"),
    path('xero/', views.xero,name="index"),
]