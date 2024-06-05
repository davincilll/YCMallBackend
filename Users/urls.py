from django.urls import path

from Users import views

urlpatterns = [
    path(r'login', views.login),
    path('register', views.register),
]
