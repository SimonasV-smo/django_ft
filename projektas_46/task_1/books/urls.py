from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),  # Knygų sąrašas
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Vienos knygos peržiūra
    path('prideti/', BookCreateView.as_view(), name='book_create'),  # Naujos knygos pridėjimas
]