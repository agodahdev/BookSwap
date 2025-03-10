from django.urls import path
from .views import book_list
from .views import add_book

urlpatterns = [
    path('', book_list, name='book_list'),  # List all books
    path('add/', add_book, name='add_book'),  # URL for adding books
]