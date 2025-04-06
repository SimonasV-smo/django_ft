from django.shortcuts import render
from .forms import NuotraukaForm
from .models import Nuotrauka

def ikelti_nuotrauka(request):
    if request.method == 'POST':
        forma = NuotraukaForm(request.POST, request.FILES)
        if forma.is_valid():
            forma.save()
            nauja_nuotrauka = forma.instance
            return render(request, 'nuotraukos/ikelti.html', {'forma': forma, 'nuotrauka': nauja_nuotrauka})
    else:
        forma = NuotraukaForm()
    return render(request, 'nuotraukos/ikelti.html', {'forma': forma})