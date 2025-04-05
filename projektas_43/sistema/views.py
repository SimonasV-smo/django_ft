from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Registracijos funkcija
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Nukreipiame vartotoją į prisijungimo puslapį
    else:
        form = UserCreationForm()
    return render(request, 'sistema/register.html', {'form': form})

# Pagrindinio puslapio funkcija
@login_required(login_url='login')  # Nukreipia vartotoją į prisijungimo puslapį, jei jis nėra prisijungęs
def home_view(request):
    return render(request, 'sistema/home.html', {'user': request.user})

# Atsijungimo funkcija
def logout_view(request):
    logout(request)  # Django atsijungimo funkcija
    return redirect('login')  # Nukreipiame vartotoją į prisijungimo puslapį