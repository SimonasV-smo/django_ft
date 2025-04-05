from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Laukas pavadinimui
    body = models.TextField()  # Laukas turiniui
    created_at = models.DateTimeField(auto_now_add=True)  # Sukūrimo laikas

    def __str__(self):
        return self.title  # Grąžina pavadinimą kaip tekstą