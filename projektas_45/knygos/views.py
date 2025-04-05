from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Book
from .forms import BookForm

# Pagrindinis puslapis ir knygų sąrašas
def book_list_view(request):
    query = request.GET.get('q', '')  # Paieškos užklausa
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)  # Filtruojame pagal pavadinimą arba autorių
    )
    paginator = Paginator(books, 5)  # Puslapiavimas - 5 knygos viename puslapyje
    page_number = request.GET.get('page')  # Dabartinis puslapis
    page_obj = paginator.get_page(page_number)
    return render(request, 'knygos/book_list.html', {'page_obj': page_obj, 'query': query})

# Knygos pridėjimo vaizdas
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Išsaugome naują knygą
            return redirect('home')  # Nukreipiame į pagrindinį puslapį
    else:
        form = BookForm()
    return render(request, 'knygos/add_book.html', {'form': form})