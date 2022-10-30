from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('phones/', views.phones, name='phones'),
    path('tablets/', views.tablets, name='tablets'),
    path('watches/', views.watches, name='watches'),
]
