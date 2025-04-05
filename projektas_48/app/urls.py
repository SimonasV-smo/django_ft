from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_List, name='post_list'),  # Naudok tikslų funkcijos pavadinimą
]