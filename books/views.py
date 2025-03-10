from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book  # Make sure you import your Book model

def home(request):
    return render(request, 'home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def add_book(request):
    if request.method == 'POST':
        # Logic to create a new book instance (handle form submission)
        pass
    return render(request, 'books/add_book.html')

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Logic to update the book instance (handle form submission)
        pass
    return render(request, 'books/edit_book.html', {'book': book})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
