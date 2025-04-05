from django.shortcuts import render
from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas' : 'Mano Puslaplis',
        'antraste' : 'Sveiki atvyke i pradini puslapi'
    }
    return render(request,'pagrindinis.html', kontekstas)

def apie():
    return HttpResponse('Cia yra apie puslapis')
