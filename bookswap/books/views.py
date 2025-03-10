from django.shortcuts import render
from .models import Book  # Import Book model
from django.contrib.auth.decorators import login_required
from .forms import BookForm

# View for listing all books
def book_list(request):
    books = Book.objects.all()  # Get all books from database
    return render(request, 'books/book_list.html', {'books': books})  # Render template with books


# View for adding a book
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user  # Assign the logged-in user as the book owner
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
