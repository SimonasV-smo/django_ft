from django.db import models

class Nuotrauka(models.Model):
    paveikslelis = models.ImageField(upload_to='nuotraukos/')  # Failų įkėlimo vieta

    def __str__(self):
        return f"Nuotrauka {self.id}"  # Patogesnis atvaizdavimas admin sąsajoje