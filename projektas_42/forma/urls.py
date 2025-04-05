from django.urls import path
from .views import registration_view, participants_view

urlpatterns = [
    path('registracija/', registration_view, name='renginiai'),
    path('dalyviai/', participants_view, name='participants'),
]