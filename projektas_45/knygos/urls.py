from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='home'),  # Pagrindinis puslapis - knygų sąrašas
    path('add/', views.add_book_view, name='add_book'),  # Maršrutas knygos pridėjimui
]