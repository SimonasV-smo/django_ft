from django.urls import path
from . import views

urlpatterns = [
    path('', views.galerija, name='home'),  # Galerija kaip pagrindinis puslapis
    path('ikelti/', views.ikelti_nuotrauka, name='ikelti_nuotrauka'),  # Maršrutas į paveikslėlio įkėlimo puslapį
]