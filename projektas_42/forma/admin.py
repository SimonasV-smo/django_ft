from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'registration_date')  # Kokie laukai bus matomi administracijoje