from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.registerHandler),
    path('login/', views.loginHandler),
]
