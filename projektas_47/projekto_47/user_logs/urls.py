from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_logs_home, name='user_logs_home'),  # Nustatome, kad pagrindinis maršrutas būtų lentelės vaizdas
]