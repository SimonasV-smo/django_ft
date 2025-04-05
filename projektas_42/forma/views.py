from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participants')  # Peradresavimas į dalyvių sąrašą
    else:
        form = RegistrationForm()
    return render(request, 'forma/renginiai.html', {'form': form})

def participants_view(request):
    participants = Registration.objects.all()
    return render(request, 'forma/participants.html', {'participants': participants})