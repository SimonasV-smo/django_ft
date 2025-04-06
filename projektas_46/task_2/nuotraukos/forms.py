from django import forms
from .models import Nuotrauka

class NuotraukaForm(forms.ModelForm):
    class Meta:
        model = Nuotrauka  # Nurodomas modelis, kurio pagrindu kuriama forma
        fields = ['paveikslelis']  # Pasirinktas laukas, kurį rodysime formoje