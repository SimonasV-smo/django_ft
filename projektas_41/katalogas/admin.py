from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('author', 'publication_date')

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
