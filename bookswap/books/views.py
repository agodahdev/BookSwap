from django.shortcuts import render, redirect, get_object_or_404
from .models import Book  # Import Book model
from django.contrib.auth.decorators import login_required
from .models import Book
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


# View for editing a book
@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Get book by ID

    # Ensure only the owner can edit
    if request.user != book.owner:
        return redirect('book_list')

    if request.method == 'POST':  # If form submitted
        form = BookForm(request.POST, instance=book)  # Pre-fill form with existing data
        if form.is_valid():  # Validate form
            form.save()  # Save updated book
            return redirect('book_list')  # Redirect to book list
    else:
        form = BookForm(instance=book)  # Show form with existing book details

    return render(request, 'books/book_form.html', {'form': form})  # Render edit template

# View for deleting a book
@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Get book by ID

    # Ensure only the owner can delete
    if request.user != book.owner:
        return redirect('book_list')

    if request.method == 'POST':  # If confirmed
        book.delete()
        return redirect('book_list')

    return render(request, 'books/book_delete.html', {'book': book})  # Render confirmation template