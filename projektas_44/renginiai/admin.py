from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'organizer')  # Rodomi stulpeliai
    search_fields = ('title', 'description')  # Paieškos laukeliai