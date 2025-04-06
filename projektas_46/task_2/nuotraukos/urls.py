from django.urls import path
from . import views

urlpatterns = [
    path('ikelti/', views.ikelti_nuotrauka, name='ikelti_nuotrauka'),
]