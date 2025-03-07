from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth_views
from .views import home, book_list, book_detail, add_book, edit_book, delete_book, signup

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('accounts/signup/', signup, name='signup'),  # Signup URL
]
