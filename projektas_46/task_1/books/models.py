from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Knygos pavadinimas
    author = models.CharField(max_length=100)  # Autorius