from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event, Registration

# Registracijos vaizdas
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Išsaugome naują vartotoją
            return redirect('login')  # Po registracijos nukreipiame į prisijungimą
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Pagrindinio puslapio vaizdas
@login_required  # Tik prisijungusiems vartotojams
def home_view(request):
    return render(request, 'renginiai/home.html')  # Naudojame šabloną "home.html"

# Renginių sąrašo vaizdas
@login_required  # Tik prisijungusiems vartotojams
def event_list_view(request):
    events = Event.objects.all()  # Gauti visus renginius
    registered_events = Registration.objects.filter(user=request.user).values_list('event_id', flat=True)  # Renginiai, kuriuose vartotojas dalyvauja
    return render(request, 'renginiai/event_list.html', {
        'events': events,
        'registered_events': registered_events,
    })

# Prisijungimas prie renginio
@login_required  # Tik prisijungusiems vartotojams
def join_event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if not Registration.objects.filter(user=request.user, event=event).exists():  # Jei vartotojas dar neprisijungęs prie renginio
        Registration.objects.create(user=request.user, event=event, comment="Prisijungta!")
    return HttpResponseRedirect(reverse('event_list'))  # Nukreipiame į renginių sąrašą