from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '')  # Paieškos užklausa
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)) if query else Book.objects.all()
        paginator = Paginator(books, 5)  # 5 knygos viename puslapyje
        page_number = self.request.GET.get('page')

        try:
            return paginator.page(page_number)
        except PageNotAnInteger:
            # Jei page_number nėra skaičius, grąžiname pirmą puslapį
            return paginator.page(1)
        except EmptyPage:
            # Jei page_number yra už diapazono, grąžiname paskutinį puslapį
            return paginator.page(paginator.num_pages)

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author']  # Laukai formoje
    success_url = reverse_lazy('home')  # Nukreipimas po pridėjimo