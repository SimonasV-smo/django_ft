from django.shortcuts import render
from .models import UserLog
from django.core.paginator import Paginator

def user_logs_home(request):
    query = request.GET.get('q')  # Paieškos užklausa
    if query:
        logs = UserLog.objects.filter(action__icontains=query)  # Filtruoti pagal veiksmą
    else:
        logs = UserLog.objects.all()  # Gauti visus duomenis

    # Puslapiavimas
    paginator = Paginator(logs, 10)  # 10 įrašų per puslapį
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user_logs/logs.html', {'logs': page_obj})  # Perduoti duomenis į šabloną