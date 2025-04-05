from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='sistema/login.html'), name='login'),  # Prisijungimo puslapis
    path('registracija/', views.register_view, name='register'),  # Registracijos puslapis
    path('atsijungti/', views.logout_view, name='logout'),  # Atsijungimo maršrutas
    path('pagrindinis/', views.home_view, name='home'),  # Pagrindinis puslapis prisijungusiems vartotojams
]