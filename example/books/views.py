from django.views.generic import ListView, DetailView

# use this import instead of short 'from .models' to escape RuntimeErros
# https://medium.com/@michal.bock/fix-weird-exceptions-when-running-django-tests-f58def71b59a
from example.books.models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

