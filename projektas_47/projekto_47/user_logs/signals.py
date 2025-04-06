from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserLog

@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if created:  # Tikrina, ar vartotojas buvo sukurtas
        UserLog.objects.create(user=instance, action="Vartotojas sukurtas")

@receiver(post_delete, sender=User)
def log_user_deletion(sender, instance, **kwargs):
    UserLog.objects.create(user=None, action=f"Vartotojas {instance.username} ištrintas")