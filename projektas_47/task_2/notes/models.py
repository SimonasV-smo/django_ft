from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)  # Pavadinimas
    content = models.TextField()  # Turinys

    def __str__(self):
        return self.title  # Atvaizduojame pavadinimą
