from django.urls import path

from .views import BookListView, BookDetailView, SearchResultView

app_name="books"

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultView.as_view(), name='search_result'),
]
