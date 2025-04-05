from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email']  # Rodomi laukai formoje

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Registration.objects.filter(email=email).exists():
            raise forms.ValidationError("Registracija su šiuo el. paštu jau yra.")
        return email