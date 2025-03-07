from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title='Sample Book', author='Author Name', condition='New', exchange_type='Swap', location='Location')

    def test_book_str(self):
        book = Book.objects.get(title='Sample Book')
        self.assertEqual(str(book), 'Sample Book')
