from django import forms
from .models import Book

# Form for adding a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'condition', 'exchange_type', 'location']