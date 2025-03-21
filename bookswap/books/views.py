from django.shortcuts import render, redirect, get_object_or_404
from .models import Book  # Import Book model
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from django.contrib import messages
from .models import BookRequest

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


# View to request a book
@login_required
def request_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Prevent users from requesting their own books
    if book.owner == request.user:
        messages.error(request, "You cannot request your own book.")
        return redirect('book_list')

    # Prevent duplicate requests
    if BookRequest.objects.filter(book=book, requester=request.user).exists():
        messages.warning(request, "You have already requested this book.")
        return redirect('book_list')

    # Create a new request
    BookRequest.objects.create(book=book, requester=request.user)
    messages.success(request, "Request sent successfully!")
    return redirect('book_list')

# View for book owners to see requests
@login_required
def view_requests(request):
    book_requests = BookRequest.objects.filter(book__owner=request.user, status='Pending')  # Get pending requests
    return render(request, 'books/book_requests.html', {'book_requests': book_requests})

# Approve a book request
@login_required
def approve_request(request, request_id):
    book_request = get_object_or_404(BookRequest, id=request_id, book__owner=request.user)
    book_request.status = 'Approved'
    book_request.save()
    return redirect('view_requests')

# Reject a book request
@login_required
def reject_request(request, request_id):
    book_request = get_object_or_404(BookRequest, id=request_id, book__owner=request.user)
    book_request.status = 'Rejected'
    book_request.save()
    return redirect('view_requests')