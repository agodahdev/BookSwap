from django.urls import path
from .views import book_list
from .views import add_book

urlpatterns = [
    path('', book_list, name='book_list'),  # List all books
    path('add/', add_book, name='add_book'),  # URL for adding books
    path('<int:book_id>/edit/', edit_book, name='edit_book'),
    path('<int:book_id>/delete/', delete_book, name='delete_book'),
    path('<int:book_id>/request/', request_book, name='request_book'),
    path('requests/', view_requests, name='view_requests'),
    path('requests/<int:request_id>/approve/', approve_request, name='approve_request'),
    path('requests/<int:request_id>/reject/', reject_request, name='reject_request'),
]