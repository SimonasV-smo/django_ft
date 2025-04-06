from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import NuotraukaForm
from .models import Nuotrauka

# Funkcija įkelti nuotrauką
def ikelti_nuotrauka(request):
    if request.method == 'POST':  # Jei užklausa POST
        forma = NuotraukaForm(request.POST, request.FILES)
        if forma.is_valid():  # Jei forma užpildyta teisingai
            forma.save()  # Išsaugo įkeltą nuotrauką
            return redirect('home')  # Grįžtame į galeriją po įkėlimo
    else:
        forma = NuotraukaForm()
    return render(request, 'nuotraukos/ikelti.html', {'forma': forma})

# Funkcija galerijai
def galerija(request):
    nuotraukos = Nuotrauka.objects.all()  # Gauti visas nuotraukas
    paginator = Paginator(nuotraukos, 6)  # 6 nuotraukos per puslapį
    page_number = request.GET.get('page')  # Dabartinio puslapio numeris
    page_obj = paginator.get_page(page_number)
    return render(request, 'nuotraukos/galerija.html', {'page_obj': page_obj})