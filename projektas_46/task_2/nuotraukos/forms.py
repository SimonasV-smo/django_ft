from django import forms
from .models import Nuotrauka

class NuotraukaForm(forms.ModelForm):
    class Meta:
        model = Nuotrauka
        fields = ['paveikslelis']  # Rodyti formoje