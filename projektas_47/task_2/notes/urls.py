from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),  # Užrašų sąrašas
    path('create/', views.notes_create, name='notes_create'),  # Užrašo kūrimas
    path('edit/<int:pk>/', views.notes_edit, name='notes_edit'),  # Užrašo redagavimas
    path('delete/<int:pk>/', views.notes_delete, name='notes_delete'),  # Užrašo ištrynimas
]