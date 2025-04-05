from django.shortcuts import render
from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas' : 'Mano Puslaplis',
        'antraste' : 'Sveiki atvyke i pradini puslapi'
    }
    return render(request,'pagrindinis.html', kontekstas)

def apie(request):
    info = {
        'pavadinimas' : 'Apie mus',
        'antraste' : 'Visa reikalinga informacija apie mus'
    }
    return render(request,'apie.html', info)

def kontaktai(request):
    return HttpResponse('Susisiek su mumis!')

def naujienos(request):
    zinios = {
        'pavadinimas' : 'Naujienos',
        'antraste' : 'Svieziausios naujienos'
    }
    return render(request,'naujienos.html', zinios)

def autorius(request):
    hobbies = {
        'vardas': 'Jonas',
        'pomegiai': ['Programavimas', 'Dviračiai', 'Kava']
    }
    return render(request,'autorius.html', hobbies)