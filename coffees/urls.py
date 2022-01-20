from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'coffees'
urlpatterns = [
    # ex: /coffees/
    path('', views.index, name='index'),
    # ex: /coffees/1/
    path('<int:pk>/', views.show, name='show'),
    # ex: /coffees/add/
    path('add/', views.add, name='add'),
    # ex: /coffees/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # ex: /coffees/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
]


