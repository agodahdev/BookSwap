from django.shortcuts import render
from .models import Book  # Import Book model

# View for listing all books
def book_list(request):
    books = Book.objects.all()  # Get all books from database
    return render(request, 'books/book_list.html', {'books': books})  # Render template with books
