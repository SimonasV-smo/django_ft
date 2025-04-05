from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)  # Dalintojas įves vardą
    email = models.EmailField(unique=True)  # El. paštas turi būti unikalus
    registration_date = models.DateTimeField(auto_now_add=True)  # Automatinė data

    def __str__(self):
        return f"{self.name} ({self.email})"