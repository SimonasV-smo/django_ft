from django.db import models
from django.contrib.auth.models import User

class UserLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # Leidžia nustatyti NULL reikšmę, kai vartotojas ištrinamas
        null=True,  # Leidžia NULL reikšmes
        blank=True,  # Leidžia lauką būti neprivalomu
        default=None  # Užtikrina saugų numatytąjį elgesį
    )
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} ({self.timestamp}) - {self.user.username if self.user else 'Nėra vartotojo'}"