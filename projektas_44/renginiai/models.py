from django.db import models
from django.contrib.auth.models import User

# Renginio modelis
class Event(models.Model):
    title = models.CharField(max_length=255)  # Renginio pavadinimas
    description = models.TextField()  # Renginio aprašymas
    date = models.DateField()  # Renginio data
    organizer = models.ForeignKey(User, on_delete=models.PROTECT)  # Renginio organizatorius

    def __str__(self):
        return self.title  # Grąžiname renginio pavadinimą

# Registracijos modelis
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Dalyvis (vartotojas)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Dalyvaujamas renginys
    comment = models.TextField(blank=True, null=True)  # Papildomas komentaras (neprivalomas)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"