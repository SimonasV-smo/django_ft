from django.db import models

class Nuotrauka(models.Model):
    paveikslelis = models.ImageField(upload_to='nuotraukos/')  # Įkėlimo vieta

    def __str__(self):
        return f"Nuotrauka {self.id}"