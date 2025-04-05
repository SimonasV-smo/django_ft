from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagrindinis, name='pagrindinis'),
    path('apie/', views.apie, name='apie'),
    path('kontaktai/', views.kontaktai, name='kontaktai'),
    path('naujienos/', views.naujienos, name='naujienos'),
    path('autorius/', views.autorius, name='autorius')
]