from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # Knygos pavadinimas
    author = models.CharField(max_length=255)  # Autorius
    description = models.TextField()  # Aprašymas

    def __str__(self):
        return f"{self.title} by {self.author}"